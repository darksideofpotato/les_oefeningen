class Gebruiker:
    # om een object te kunnen maken van de klasse gebruiker
    def __init__(self, naam, score):
        self.naam = naam
        self.score = score

    # functie om de gebruikersnaam aan de passen naar de ingevoerde waarde
    # past tot nu toe alles aan waar de waarde van self.naam in voorkomt
    # kan voor problemen zorgen
    def set_gebruikersnaam(self, gebruikersnaam):
        accounts = open("inleveropdracht_1_accounts.txt", "rt")
        data = accounts.read()
        data = data.replace(self.naam, gebruikersnaam)
        accounts.close()

        accounts = open("inleveropdracht_1_accounts.txt", "wt")
        accounts.write(data)
        accounts.close()

        self.naam = gebruikersnaam
        # pas op met cijfers

    # functie om de score aan te passen na een goed antwoord op een quizvraag.
    # pakt de huidige score en telt daar 10 bij op, om dit vervolgens te verwerken
    # in de textfile
    def set_score(self, ing_score):

        scores = open("inleveropdracht_1_accounts.txt", "rt")
        string_score = str(self.score + int(ing_score))
        data = scores.read()
        data = data.replace(self.naam + " " + str(self.score), self.naam + " " + string_score)
        scores.close()

        scores = open("inleveropdracht_1_accounts.txt", "wt")
        scores.write(data)
        scores.close()

        self.score = self.score + int(ing_score)

    # functie om de gebruikersnaam en score van een gebruiker te weergeven,
    # wordt gebruikt bij de menu optie om gegevens te bekijken en aan te passen
    def display_details(self):
        print("Je gebruikersnaam is " + str(self.naam) +
              "\nJe huidige score is " + str(self.score))

    # functie om de username op te vragen en te returnen.
    def get_username(self):
        return self.naam

    # functie om in te loggen, alle gebruikersnamen worden in een list
    # gestopt en vergeleken met de waarde die ingevoerd is. Als de waarde gelijk is,
    # wordt ingelogd met dat account. Anders wordt een nieuw account aangemaakt
    # en wordt daarmee ingelogd
    def login(self, naam):
        accounts = open("inleveropdracht_1_accounts.txt", "r")
        lijst_met_namen = []
        lijst_met_gebruikers = []

        for x in accounts:
            lijst_met_gebruikers.append(x.split())

        # try/except indexerrors zijn gemaakt zodat bij een leeg bestand het programma gewoon verder kan werken.
        for y in lijst_met_gebruikers:
            try:
                lijst_met_namen.append(y[0])
            except IndexError:
                pass

        for p in lijst_met_gebruikers:
            try:
                if p[0] == naam:
                    score_gebruiker = p[1]
                    self.set_score(score_gebruiker)
            except IndexError:
                pass

        if naam in lijst_met_namen:
            print("hoi, " + str(naam) + " je score is " + score_gebruiker)
        else:
            namen2 = open("inleveropdracht_1_accounts.txt", "a")
            namen2.write("\n" + naam + " " + str(self.score))
            accounts.close()
            print("Welkom, " + naam + ". er is een nieuw account voor je aangemaakt")

    # met de functie logout wordt de gebruiker "uitgelogd"; teruggebracht naar
    # het beginscherm
    def logout(self):
        start_program()

    # een nieuw object wordt aangemaakt op basis van de door de gebruiker ingevoerde
    # waarden. Vervolgens wordt de functie binnen LosseVraag aangeroepen om de vraag
    # in de .txt file te verwerken
    def maak_losse_vraag(self):
        lijst_van_themas = []
        beschikbare_themas = []
        themas = open("inleveropdracht_1_themas.txt", "rt")
        for thema in themas:
            beschikbare_themas.append(thema)

        flag = True

        vraagtitel = input("Wat is de titel van je vraag?")
        antwoordvraag = input("Wat is het antwoord bij de vraag?")

        print("De volgende thema's bestaan al")
        for thema in beschikbare_themas:
            print(thema)
        bestaand_thema_kiezen = input("Wil je hier een of meerderen uit kiezen? (y/n)")
        if bestaand_thema_kiezen == 'y':
            for thema in beschikbare_themas:
                input_bestaand_thema_toevoegen = input("Wil je thema " + thema + " toevoegen? (y/n)")
                if input_bestaand_thema_toevoegen == "y":
                    lijst_van_themas.append(thema)
        else:
            pass

        while flag:
            themas_toevoegen = input("Wil je zelf nog themas toevoegen? (enter voor nee, thema intypen voor ja)")
            if themas_toevoegen == "":
                flag = False
            else:
                lijst_van_themas.append(themas_toevoegen)
                themas = open("inleveropdracht_1_themas.txt", "a")
                themas.write("\n" + themas_toevoegen)

        type = input("Wat voor type vraag is het?")

        new_question = LosseVraag(vraagtitel, type, lijst_van_themas, antwoordvraag, the_user)
        new_question.opslaan_vraag()