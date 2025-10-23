
liste_haltestellen = ["A", "B", "C", "D", "E", "F", "G", "H"]
while True:
    # Eingaben in Großbuchstaben umwandeln
    start = input("Geben Sie Ihre Starthaltestelle an: ").upper()
    ziel = input("Geben Sie Ihre Zielhaltestelle an: ").upper()
    print()
    if start == ziel:
        print("Gleiche Haltestellen nicht möglich")
        continue
    # Test, Eingabe entspricht den Werten in der Liste?
    start_korrekt = False
    ziel_korrekt = False
    for i in range(len(liste_haltestellen)):
        if start == liste_haltestellen[i]:
            start_korrekt = True
        if ziel == liste_haltestellen[i]:
            ziel_korrekt = True

    if start_korrekt == False or ziel_korrekt == False:
        print("Eingabe war fehlerhaft!")
        continue
    if start_korrekt == True and ziel_korrekt == True:
        break
print(f"Sie fahren los von {start} und fahren bis {ziel}.")
# Index ermitteln
start_index = liste_haltestellen.index(start)
ziel_index = liste_haltestellen.index(ziel)
# Abstand ermitteln zwischen zwei Haltestellen
if start_index < ziel_index:
    abstand = ziel_index - start_index
elif ziel_index < start_index:
    abstand = start_index - ziel_index
# Test
#print(abstand)
# Voraussetzungen für ein Kurzstreckenticket prüfen
if abstand <= 3:
    print("Kurzstreckenticket: OK.")
else:
    print("Kein Kurzstreckenticket.")









###Liste_Haltestellen ← ["A", "B", "C", "D", "E", "F", "G", "H"]
'''
Wiederhole unendlich oft:
    START ← Eingabe("Geben Sie Ihre Starthaltestelle an:") in Großbuchstaben
    ZIEL  ← Eingabe("Geben Sie Ihre Zielhaltestelle an:") in Großbuchstaben
    
    Wenn START = ZIEL dann:
        Ausgabe("Gleiche Haltestellen nicht möglich")
        Fahre mit nächster Schleifeniteration fort
    
    START_KORREKT ← FALSCH
    ZIEL_KORREKT  ← FALSCH

    Für i von 0 bis Länge(Liste_Haltestellen) - 1:
        Wenn START = Liste_Haltestellen[i] dann:
            START_KORREKT ← WAHR
        Wenn ZIEL = Liste_Haltestellen[i] dann:
            ZIEL_KORREKT ← WAHR
    Ende Für

    Wenn START_KORREKT = FALSCH oder ZIEL_KORREKT = FALSCH dann:
        Ausgabe("Eingabe war fehlerhaft!")
        Fahre mit nächster Schleifeniteration fort
    
    Wenn START_KORREKT = WAHR und ZIEL_KORREKT = WAHR dann:
        Beende die Schleife
Ende Wiederhole

Ausgabe("Sie fahren los von", START, "und fahren bis", ZIEL)

START_INDEX ← Position von START in Liste_Haltestellen
ZIEL_INDEX  ← Position von ZIEL in Liste_Haltestellen

Wenn START_INDEX < ZIEL_INDEX dann:
    ABSTAND ← ZIEL_INDEX - START_INDEX
Sonst:
    ABSTAND ← START_INDEX - ZIEL_INDEX
Ende Wenn

Ausgabe("Abstand:", ABSTAND)

Wenn ABSTAND ≤ 3 dann:
    Ausgabe("Kurzstreckenticket: OK.")
Sonst:
    Ausgabe("Kein Kurzstreckenticket.")
Ende Wenn'''