import random
import csv
import selection_pool_1
import Funktion_Generieren  # enthält Generieren() und Generieren_fehlerhaft()

def main():
    alle_eintraege = []

    for i in range(len(selection_pool_1.verlagsnamen)):
        wahl = random.randint(1, 10)  # 1–10

        if wahl == 1:
            # Fehlerhafte Generierung
            eintrag = Funktion_Generieren.Generieren_fehlerhaft_auto(i + 1)
            if eintrag:
                alle_eintraege.append(eintrag)
        else:
            # Korrekte Generierung
            eintrag = Funktion_Generieren.Generieren_auto(i + 1)
            if eintrag:
                alle_eintraege.append(eintrag)

        i += 1

    # CSV speichern
    csv_datei = "verlagsdaten.csv"
    with open(csv_datei, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Verlag", "Adresse", "Kontaktperson", "Telefonnummer"])
        writer.writerows(alle_eintraege)

    print(f"\nAlle Einträge wurden in '{csv_datei}' gespeichert.")
    print(f"Anzahl der Einträge: {len(alle_eintraege)}")

if __name__ == "__main__":
    main()