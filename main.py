# De standaardprijs van een auto
startprijs = 7500
totaalprijs = startprijs

# Namen auto onderdelen
auto_onderdelen = ["merk", "model", "motor", "kleur",
                     "uitvoering", "extra opties", "interieur"]

# De gekozen meerprijzen hier later bewaren
gekozen_meerprijzen = []

# Automerken
merken = {
    "toyota": 0,
    "volkswagen": 200,
    "ford": 300,
    "volvo": 400,
    "hyundai": 500,
    "tesla": 600,
    "audi": 700,
    "bmw": 800
}

# Automodellen
modellen = {
    "compact": 0,
    "hatchback": 200,
    "sedan": 300,
    "suv": 500,
    "sport": 700,
    "family": 800
}

# Motorsoorten
motorsoorten = {
    "benzine": 0,
    "diesel": 100,
    "hybride": 300,
    "plug-in hybride": 450,
    "elektrisch": 600
}

# Autokleuren
kleuren = {
    "wit": 0,
    "zwart": 100,
    "donkerblauw": 150,
    "zilver": 200,
    "donkergroen": 250,
    "bordeauxrood": 300,
    "matgrijs": 400,
    "goud": 500
}

# Uitvoeringen
uitvoeringen = {
    "basic": 0,
    "comfort": 200,
    "premium": 400,
    "sport": 600,
    "exclusive": 800
}

# Extra opties
extra_opties = {
    "geen": 0,
    "dakdragers": 75,
    "navigatiesysteem": 150,
    "parkeersensoren": 175,
    "achteruitrijcamera": 200,
    "panoramadak": 350,
    "sportvelgen": 400,
    "trekhaak": 250
}

# Interieursoorten
interieurs = {	
    "stof": 0,
    "kunstleder": 150,
    "leder": 300,
    "alcantara": 400,
    "sportinterieur": 500
}


# Hoofdmenu
print("\nWELKOM BIJ AUTOFACTORY")
print("1. Nieuwe auto samenstellen")
print("2. Afsluiten")

keuze = input("Wat wilt u doen? (1/2): ").lower()

if keuze == "1":
    print("\nLeuk! We gaan een auto samenstellen.")

elif keuze == "2":
    print("\nBedankt voor uw bezoek aan AutoFactory!")

else:
    print("\nOngeldige keuze. Kies 1 of 2.")


if keuze == "1":
    print("\nBeschikbare automerken:")

 # Automerk kiezen
    for merk, meerprijs in merken.items():
        print(merk.title(), "- Meerprijs: €", meerprijs)

    gekozen_merk = input("\nWelk automerk wilt u kiezen? ").lower()

    while gekozen_merk not in merken:
        print("Dit automerk is niet beschikbaar.")
        gekozen_merk = input("Kies een automerk uit de lijst: ").lower()

    merkprijs = merken.get(gekozen_merk)
    totaalprijs += merkprijs

    print("\nU heeft gekozen voor:", gekozen_merk.title())
    print("Huidige totaalprijs: €", totaalprijs)

    # Automodel kiezen
    print("\nBeschikbare automodellen:")

    for model, meerprijs in modellen.items():
        print(model.title(), "- Meerprijs: €", meerprijs)

    gekozen_model = input("\nWelk automodel wilt u kiezen? ").lower()

    while gekozen_model not in modellen:
        print("Dit automodel is niet beschikbaar.")
        gekozen_model = input("Kies een automodel uit de lijst: ").lower()

    modelprijs = modellen.get(gekozen_model)
    totaalprijs += modelprijs

    print("U heeft gekozen voor:", gekozen_model.title())

    # Motor kiezen
    print("\nBeschikbare motorsoorten:")

    for motor, meerprijs in motorsoorten.items():
        print(motor.title(), "- Meerprijs: €", meerprijs)

    gekozen_motor = input("\nWelke motorsoort wilt u kiezen? ").lower()

    while gekozen_motor not in motorsoorten:
        print("Deze motorsoort is niet beschikbaar.")
        gekozen_motor = input("Kies een motorsoort uit de lijst: ").lower()

    motorprijs = motorsoorten.get(gekozen_motor)
    totaalprijs += motorprijs

    print("U heeft gekozen voor:", gekozen_motor.title())

    # Kleur kiezen
    print("\nBeschikbare kleuren:")

    for kleur, meerprijs in kleuren.items():
        print(kleur.title(), "- Meerprijs: €", meerprijs)

    gekozen_kleur = input("\nWelke kleur wilt u kiezen? ").lower()

    while gekozen_kleur not in kleuren:
        print("Deze kleur is niet beschikbaar.")
        gekozen_kleur = input("Kies een kleur uit de lijst: ").lower()

    kleurprijs = kleuren.get(gekozen_kleur)
    totaalprijs += kleurprijs

    print("U heeft gekozen voor:", gekozen_kleur.title())

    # Uitvoering kiezen
    print("\nBeschikbare uitvoeringen:")

    for uitvoering, meerprijs in uitvoeringen.items():
        print(uitvoering.title(), "- Meerprijs: €", meerprijs)

    gekozen_uitvoering = input("\nWelke uitvoering wilt u kiezen? ").lower()

    while gekozen_uitvoering not in uitvoeringen:
        print("Deze uitvoering is niet beschikbaar.")
        gekozen_uitvoering = input("Kies een uitvoering uit de lijst: ").lower()

    uitvoeringprijs = uitvoeringen.get(gekozen_uitvoering)
    totaalprijs += uitvoeringprijs

    print("U heeft gekozen voor:", gekozen_uitvoering.title())

    # Interieur kiezen
    print("\nBeschikbare interieurs:")

    for interieur, meerprijs in interieurs.items():
        print(interieur.title(), "- Meerprijs: €", meerprijs)

    gekozen_interieur = input("\nWelk interieur wilt u kiezen? ").lower()

    while gekozen_interieur not in interieurs:
        print("Dit interieur is niet beschikbaar.")
        gekozen_interieur = input("Kies een interieur uit de lijst: ").lower()

    interieurprijs = interieurs.get(gekozen_interieur)
    totaalprijs += interieurprijs

    print("U heeft gekozen voor:", gekozen_interieur.title())

    # Extra opties kiezen
    print("\nBeschikbare extra opties:")

    for optie, meerprijs in extra_opties.items():
        print(optie.title(), "- Meerprijs: €", meerprijs)

    print("\nUw auto kan meerdere extra opties krijgen.")
    print("Typ 'stop' wanneer u klaar bent.")

    gekozen_opties = []

    gekozen_optie = input("\nWelke extra optie wilt u toevoegen? ").lower()

    while gekozen_optie != "stop":

        if gekozen_optie in extra_opties:
            optieprijs = extra_opties.get(gekozen_optie)
            totaalprijs += optieprijs
            gekozen_opties.append(gekozen_optie)

            print("Extra optie toegevoegd!")

        else:
            print("Deze optie is niet beschikbaar.")

        gekozen_optie = input("Kies nog een optie of typ 'stop': ").lower()

    print("\nAlle keuzes zijn gemaakt!")
    print("Huidige totaalprijs: €", totaalprijs)

elif keuze == "2":
    print("\nBedankt voor uw bezoek aan AutoFactory!")

else:
    print("\nOngeldige keuze. Kies 1 of 2.")