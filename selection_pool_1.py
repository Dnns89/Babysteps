from faker import Faker



verlagsnamen = [
    "Rowohlt Verlag",
    "Suhrkamp Verlag",
    "Fischer Verlage",
    "dtv Verlagsgesellschaft",
    "C.H. Beck",
    "Hanser Verlag",
    "Kiepenheuer & Witsch",
    "Droemer Knaur",
    "Heyne Verlag",
    "Piper Verlag",
    "Carlsen Verlag",
    "Ullstein Buchverlage",
    "Campus Verlag",
    "Goldmann Verlag",
    "O'Reilly Media",
    "Springer Fachmedien",
    "Reclam Verlag",
    "Thienemann-Esslinger",
    "Cornelsen Verlag",
    "Beltz & Gelberg",
    "Bastei Lübbe",
    "Bonnier Verlagsgruppe",
    "Cornelsen Verlag",
    "Eulenspiegel Verlagsgruppe",
    "Hubert Burda Media",
    "Hans Gerig Musikverlage",
    "Haufe Mediengruppe",
    "Ernst Klett Verlag",
    "MairDumont",
    "Medien Union",
    "Münchner Verlagsgruppe",
    "Südwestdeutsche Medien Holding",
    "Verlag C.H. Beck",
    "Verlagsgruppe Georg von Holtzbrinck",
    "Verlagsgruppe Handelsblatt",
    "Verlagsgruppe Herder",
    "Verlagsgruppe Husum",
    "Verlagsgruppe Hüthig Jehle Rehm",
    "Verlagsgruppe Ippen",
    "Verlagsgruppe Random House",
    "Verlagsgruppe Weltbild",
    "Verlagshaus Römerweg",
    "WEKA-Verlagsgruppe",
    "Verlag Moderne Industrie",
    "Redline Verlag",
    "Nomos Verlagsgesellschaft",
    "Oldenbourg Verlag",
    "Verlag J. Neumann",
    "Reinhold Kühn Verlag",
    "Münchener Verlagsgruppe",
    "Verlag Gerhard Rautenberg",
    "Silberschnur Verlag",
    "SingLiesel Verlag",
    "Thomas Kettler Verlag",
    "MM Verlag",
    "Diederichs Verlag",
    "Gräfe und Unzer Verlag"
    ]

# seed festlegen:
Faker.seed(12345)
# Namenslisten generieren
fake_namen = Faker('de_DE')

vornamen = [f"{fake_namen.first_name()}" for i in range(100)]
nachnamen = [f"{fake_namen.last_name()}" for i in range(100)]

# Adressliste genereiren
fake_adressen = Faker('de_DE')

adressen = []
for i in range(len(verlagsnamen)):
    adresse = fake_adressen.address().replace("\n", ", ")
    adressen.append(adresse)

# Telefonnummernliste generieren
fake_telefonnummern = Faker('de_DE')

telefonnummern = [f"{fake_telefonnummern.phone_number()}" for i in range(len(verlagsnamen))]

for i in range(10):
    print(f"i: {i} - namen: {vornamen[i]} {nachnamen[i]}, {adressen[i]}, {telefonnummern[i]}")


##seed test 1
# i: 0 - namen: Serge Ehlert, Weimerplatz 6283, 28804 Bad Liebenwerda, 04342 87215
# i: 1 - namen: Janna Berger, Gerolf-Köhler-Allee 4, 56479 Heinsberg, +49(0)0292 018259
# i: 2 - namen: Albin Gehringer, Joseph-Matthäi-Gasse 2520, 19367 Guben, 01014627476
# i: 3 - namen: Mariana Jacobi Jäckel, van der Dussenring 2-5, 06321 Havelberg, +49(0)7221 68656
# i: 4 - namen: Marieluise Anders, Gutegasse 118, 65031 Dresden, 0004944026
# i: 5 - namen: Madlen Fischer, Freudenbergerweg 1/2, 83886 Parchim, 0620058677
# i: 6 - namen: Kornelius Hein, Utz-Liebelt-Straße 5, 65890 München, +49(0) 384968416
# i: 7 - namen: Nadeschda Killer, Johannstraße 3/7, 91711 Bad Brückenau, (01591) 82614
# i: 8 - namen: Paul Reuter, Annelene-Dietz-Straße 77-40, 52698 Torgau, (02520) 81443
# i: 9 - namen: Swantje Karz, Birgitta-Ruppert-Weg 4270, 18114 Fulda, 0904592348
##seed test 2
# i: 0 - namen: Serge Ehlert, Weimerplatz 6283, 28804 Bad Liebenwerda, 04342 87215
# i: 1 - namen: Janna Berger, Gerolf-Köhler-Allee 4, 56479 Heinsberg, +49(0)0292 018259
# i: 2 - namen: Albin Gehringer, Joseph-Matthäi-Gasse 2520, 19367 Guben, 01014627476
# i: 3 - namen: Mariana Jacobi Jäckel, van der Dussenring 2-5, 06321 Havelberg, +49(0)7221 68656
# i: 4 - namen: Marieluise Anders, Gutegasse 118, 65031 Dresden, 0004944026
# i: 5 - namen: Madlen Fischer, Freudenbergerweg 1/2, 83886 Parchim, 0620058677
# i: 6 - namen: Kornelius Hein, Utz-Liebelt-Straße 5, 65890 München, +49(0) 384968416
# i: 7 - namen: Nadeschda Killer, Johannstraße 3/7, 91711 Bad Brückenau, (01591) 82614
# i: 8 - namen: Paul Reuter, Annelene-Dietz-Straße 77-40, 52698 Torgau, (02520) 81443
# i: 9 - namen: Swantje Karz, Birgitta-Ruppert-Weg 4270, 18114 Fulda, 0904592348