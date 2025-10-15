import random
import selection_pool_1


# -----------------------------
# Funktion 1: korrekte Datensätze
# -----------------------------
def Generieren():
    """
    Liest eine ID ein (1.len(selection_pool_1.verlagsnamen)),
    erzeugt einen vollständigen, korrekten Eintrag auf Basis der Listen
    in selection_pool_1 und entfernt Adresse / Nachname / Telefonnummer
    aus den Pools, damit sie nicht erneut verwendet werden.

    Rückgabe: [id, name, adresse, kontaktperson, telefonnummer]
    """
    # ID einlesen und prüfen
    try:
        raw = input(f"Bitte ID eingeben (1–{len(selection_pool_1.verlagsnamen)}): ")
        id_num = int(raw)
    except ValueError:
        print("Ungültige Eingabe: Bitte eine ganze Zahl eingeben.")
        return None

    if not (1 <= id_num <= len(selection_pool_1.verlagsnamen)):
        print("Ungültige ID: außerhalb des erlaubten Bereichs.")
        return None

    # Name (Verlag) auswählen (index-basiert)
    name = selection_pool_1.verlagsnamen[id_num - 1]

    # Hilfsfunktion: sichere Wahl aus Liste mit aussagekräftiger Fehlermeldung
    def _safe_choice_and_remove(pool, pool_name):
        if not pool:
            raise RuntimeError(f"Pool '{pool_name}' ist leer — kann keinen Wert wählen.")
        choice = random.choice(pool)
        pool.remove(choice)
        return choice

    try:
        adresse = _safe_choice_and_remove(selection_pool_1.adressen, "adressen")
        nachname = _safe_choice_and_remove(selection_pool_1.nachnamen, "nachnamen")
        vorname = random.choice(selection_pool_1.vornamen) if selection_pool_1.vornamen else ""
        telefonnummer = _safe_choice_and_remove(selection_pool_1.telefonnummern, "telefonnummern")
    except RuntimeError as e:
        print("Fehler beim Generieren:", e)
        return None

    kontaktperson = f"{vorname} {nachname}".strip()

    eintrag = [id_num, name, adresse, kontaktperson, telefonnummer]

    # Ausgabe (übersichtlich)
    print("\n✅ --- Generierter Eintrag ---")
    print(f"ID:              {id_num}")
    print(f"Verlag:          {name}")
    print(f"Adresse:         {adresse}")
    print(f"Kontaktperson:   {kontaktperson}")
    print(f"Telefonnummer:   {telefonnummer}")
    print("------------------------------\n")

    return eintrag


# -----------------------------
# Funktion 2: fehlerhafte Datensätze
# -----------------------------
def Generieren_fehlerhaft():
    """
    Erzeugt einen fehlerhaften Eintrag:
    - Adresse wird zuerst in Bytes kodiert und dann in Latin-1 dekodiert
    - Kontaktperson wird ebenso in Bytes und Latin-1 konvertiert
    - Ansonsten wie Generieren()
    """
    try:
        raw = input(f"Bitte ID eingeben (1–{len(selection_pool_1.verlagsnamen)}): ")
        id_num = int(raw)
    except ValueError:
        print("Ungültige Eingabe: Bitte eine ganze Zahl eingeben.")
        return None

    if not (1 <= id_num <= len(selection_pool_1.verlagsnamen)):
        print("Ungültige ID: außerhalb des erlaubten Bereichs.")
        return None

    name = selection_pool_1.verlagsnamen[id_num - 1]

    # Adresse zufällig auswählen & entfernen
    if not selection_pool_1.adressen:
        print("Fehler: Adressliste leer")
        return None
    adresse = random.choice(selection_pool_1.adressen)
    selection_pool_1.adressen.remove(adresse)

    # Adresse in Bytes und dann Latin-1 (absichtlich "fehlerhaft")
    adresse_bytes = adresse.encode("utf-8")
    adresse_latin1 = adresse_bytes.decode("latin1")

    # Nachname und Vorname
    if not selection_pool_1.nachnamen:
        print("Fehler: Nachnamenliste leer")
        return None
    nachname = random.choice(selection_pool_1.nachnamen)
    selection_pool_1.nachnamen.remove(nachname)

    vorname = random.choice(selection_pool_1.vornamen) if selection_pool_1.vornamen else ""

    kontaktperson = f"{vorname} {nachname}".strip()
    kontaktperson_bytes = kontaktperson.encode("utf-8")
    kontaktperson_latin1 = kontaktperson_bytes.decode("latin1")

    # Telefonnummer
    if not selection_pool_1.telefonnummern:
        print("Fehler: Telefonnummernliste leer")
        return None
    telefonnummer = random.choice(selection_pool_1.telefonnummern)
    selection_pool_1.telefonnummern.remove(telefonnummer)

    # Eintrag erstellen
    eintrag = [id_num, name, adresse_latin1, kontaktperson_latin1, telefonnummer]

    # Ausgabe
    print("\n⚠️ --- FEHLERHAFTER EINTRAG ---")
    print(f"ID:              {id_num}")
    print(f"Verlag:          {name}")
    print(f"Adresse (Latin1):{adresse_latin1}")
    print(f"Kontaktperson:   {kontaktperson_latin1}")
    print(f"Telefonnummer:   {telefonnummer}")
    print("-------------------------------\n")

    return eintrag

def Generieren_auto(id_num):
    """
    Automatische Version von Generieren() ohne ID-Eingabe.
    """
    name = selection_pool_1.verlagsnamen[id_num - 1]

    def _safe_choice_and_remove(pool, pool_name):
        if not pool:
            raise RuntimeError(f"Pool '{pool_name}' ist leer — kann keinen Wert wählen.")
        choice = random.choice(pool)
        pool.remove(choice)
        return choice

    try:
        adresse = _safe_choice_and_remove(selection_pool_1.adressen, "adressen")
        nachname = _safe_choice_and_remove(selection_pool_1.nachnamen, "nachnamen")
        vorname = random.choice(selection_pool_1.vornamen) if selection_pool_1.vornamen else ""
        telefonnummer = _safe_choice_and_remove(selection_pool_1.telefonnummern, "telefonnummern")
    except RuntimeError as e:
        print("Fehler beim Generieren:", e)
        return None

    kontaktperson = f"{vorname} {nachname}".strip()
    eintrag = [id_num, name, adresse, kontaktperson, telefonnummer]

    print("\n✅ --- Generierter Eintrag ---")
    print(f"ID: {id_num}, Verlag: {name}, Adresse: {adresse}, Kontaktperson: {kontaktperson}, Telefonnummer: {telefonnummer}")
    return eintrag


def Generieren_fehlerhaft_auto(id_num):
    """
    Automatische Version von Generieren_fehlerhaft() ohne ID-Eingabe.
    """
    name = selection_pool_1.verlagsnamen[id_num - 1]

    if not selection_pool_1.adressen:
        print("Fehler: Adressliste leer")
        return None
    adresse = random.choice(selection_pool_1.adressen)
    selection_pool_1.adressen.remove(adresse)
    adresse_latin1 = adresse.encode("utf-8").decode("latin1")

    if not selection_pool_1.nachnamen:
        print("Fehler: Nachnamenliste leer")
        return None
    nachname = random.choice(selection_pool_1.nachnamen)
    selection_pool_1.nachnamen.remove(nachname)

    vorname = random.choice(selection_pool_1.vornamen) if selection_pool_1.vornamen else ""
    kontaktperson_latin1 = f"{vorname} {nachname}".encode("utf-8").decode("latin1")

    if not selection_pool_1.telefonnummern:
        print("Fehler: Telefonnummernliste leer")
        return None
    telefonnummer = random.choice(selection_pool_1.telefonnummern)
    selection_pool_1.telefonnummern.remove(telefonnummer)

    eintrag = [id_num, name, adresse_latin1, kontaktperson_latin1, telefonnummer]

    print("\n⚠️ --- FEHLERHAFTER EINTRAG ---")
    print(f"ID: {id_num}, Verlag: {name}, Adresse(Latin1): {adresse_latin1}, Kontaktperson: {kontaktperson_latin1}, Telefonnummer: {telefonnummer}")
    return eintrag