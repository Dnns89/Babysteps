
liste_haltestellen = ["A", "B", "C", "D", "E", "F", "G", "H"]
while True:
    
    start = input("Geben Sie Ihre Starthaltestelle an: ").upper()
    ziel = input("Geben Sie Ihre Zielhaltestelle an: ").upper()
    print()
    if start == ziel:
        print("Gleiche Haltestellen nicht möglich")
        continue
    
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

start_index = liste_haltestellen.index(start)
ziel_index = liste_haltestellen.index(ziel)

if start_index < ziel_index:
    abstand = ziel_index - start_index
elif ziel_index < start_index:
    abstand = start_index - ziel_index

if abstand <= 3:
    print("Kurzstreckenticket: OK.")
else:
    print("Kein Kurzstreckenticket.")









