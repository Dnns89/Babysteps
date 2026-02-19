import json
import os
from tkinter import messagebox, simpledialog
from models import all_categories
from datetime import date
# Pfad-Konfiguration
BASE_DIR = "Trainingsplan Ordner"
USER_FILE = os.path.join(BASE_DIR, "user.json")

# Zentrales User-Objekt (Initialzustand)
user = {
    "name": None,
    "stats": {
        "plaene_erstellt": 0,
        "uebungen_absolviert": 0,
        "gesamtzeit": 0,
        "kategorien": {cat: 0 for cat in all_categories}
    },
    "week": {
        "kw": None,
        "jahr": None,
        "minuten": 0,
        "uebungen": 0,
        "plaene": 0
    },
    "ziele": {
        "woechentlich_minuten": 0,
        "woechentlich_uebungen": 0
    }
}

def check_week_reset():
    today = date.today()
    kw, jahr, _ = today.isocalendar()

    week = user.setdefault("week", {})

    # fehlende Keys absichern
    week.setdefault("kw", kw)
    week.setdefault("jahr", jahr)
    week.setdefault("minuten", 0)
    week.setdefault("uebungen", 0)
    week.setdefault("plaene", 0)

    # neue Kalenderwoche?
    if week["kw"] != kw or week["jahr"] != jahr:
        # optional: hier später Historie / Auswertung
        week["kw"] = kw
        week["jahr"] = jahr
        week["minuten"] = 0
        week["uebungen"] = 0
        week["plaene"] = 0
        save_user()


def save_user():
    """Speichert das user-Dictionary in die JSON-Datei."""
    try:
        # Ordner erstellen, falls er nicht existiert
        os.makedirs(BASE_DIR, exist_ok=True)
        with open(USER_FILE, "w", encoding="utf-8") as f:
            json.dump(user, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")


def load_user(root):
    """Lädt die Nutzerdaten und sorgt für Abwärtskompatibilität."""
    global user
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)

            # Daten mergen (verhindert Abstürze bei fehlenden Keys)
            user.update(loaded)

            # Sicherstellen, dass alle Statistik-Strukturen vorhanden sind
            stats = user.setdefault("stats", {})
            stats.setdefault("plaene_erstellt", 0)
            stats.setdefault("uebungen_absolviert", 0)
            stats.setdefault("gesamtzeit", 0)

            # Kategorien-Dict absichern
            kat_stats = stats.setdefault("kategorien", {})
            for cat in all_categories:
                kat_stats.setdefault(cat, 0)

            # Ziele absichern
            ziele = user.setdefault("ziele", {})
            ziele.setdefault("woechentlich_minuten", 0)
            ziele.setdefault("woechentlich_uebungen", 0)

            if not user.get("name"):
                ask_new_user(root)
        except Exception:
            messagebox.showwarning("Hinweis", "Daten korrupt. Erstelle neues Profil.")
            ask_new_user(root)
    else:
        ask_new_user(root)


def ask_new_user(root):
    """Initialer Dialog für neue Nutzer."""
    name = simpledialog.askstring("Neuer Nutzer", "Bitte geben Sie ihren Namen ein:", parent=root)
    user["name"] = name if name else "Unbekanntes Talent"
    save_user()


def update_stats(plan, total_duration):

    check_week_reset()
    """Verarbeitet einen absolvierten Plan in den Statistiken."""
    user["stats"]["plaene_erstellt"] += 1
    user["stats"]["uebungen_absolviert"] += len(plan)
    user["stats"]["gesamtzeit"] += total_duration

    for ex in plan:
        for cat in ex.categories:
            if cat in user["stats"]["kategorien"]:
                user["stats"]["kategorien"][cat] += 1


    week = user["week"]
    week["plaene"] += 1
    week["uebungen"] += len(plan)
    week["minuten"] += total_duration

save_user()