from collections import Counter

class Gebruiker:
    # om een object te kunnen maken van de klasse gebruiker
    def __init__(self, naam, score, aantal_gespeeld, gemaakte_vragen):
        self.naam = naam
        self.score = score
        self.aantal_gespeeld = aantal_gespeeld
        self.gemaakte_vragen = gemaakte_vragen

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
        data = data.replace(
            self.naam + "|" + str(self.score) + "|" + str(self.aantal_gespeeld) + "|" + str(self.gemaakte_vragen),
            self.naam + "|" + string_score + "|" + str(self.aantal_gespeeld) + "|" + str(self.gemaakte_vragen))
        scores.close()

        scores = open("inleveropdracht_1_accounts.txt", "wt")
        scores.write(data)
        scores.close()

        self.score = self.score + int(ing_score)

    def set_aantal_gespeeld(self, gespeeld):
        aantal = open("inleveropdracht_1_accounts.txt", "rt")
        nu_gespeeld = str(int(self.aantal_gespeeld) + int(gespeeld))
        data = aantal.read()
        data = data.replace(
            self.naam + "|" + str(self.score) + "|" + str(self.aantal_gespeeld) + "|" + str(self.gemaakte_vragen),
            self.naam + "|" + str(self.score) + "|" + nu_gespeeld + "|" + str(self.gemaakte_vragen))
        aantal.close()

        aantal = open("inleveropdracht_1_accounts.txt", "wt")
        aantal.write(data)
        aantal.close()

        self.aantal_gespeeld = int(self.aantal_gespeeld) + int(gespeeld)

    # Wanneer de gebruiker een nieuwe vraag aanmaakt, zal deze worden opgeslagen binnen gemaakte vragen van de gebruiker.
    # Om dit te realiseren zijn een aantal tussenstappen nodig geweest, zoals het ophalen en strippen van de list van
    # gemaakte vragen van de gebruiker.
    def set_gemaakte_vragen(self, nieuwe_vraag):
        vragen = open("inleveropdracht_1_accounts.txt", "r")

        lijst_van_gebruikers = []
        lijst_van_vragen = []

        for gebruiker in vragen:
            lijst_van_gebruikers.append(gebruiker.split('|'))

        for vraag in lijst_van_gebruikers:
            if vraag[0] == self.naam:
                for x in ['[', ']', '\'', '\"']:
                    vraag[3] = vraag[3].replace(x, '')
                    vraag[3] = vraag[3].replace(', ', '|')

                if '|' in vraag[3]:
                    split = vraag[3].split('|')
                    for x in split:
                        lijst_van_vragen.append(x)
                else:
                    lijst_van_vragen.append(vraag[3])

        ## Haalt de 0 weg die als placeholder wordt gebruikt wanneer er nog geen vragen zijn gemaakt
        lijst_van_vragen.append(nieuwe_vraag)
        if '0' in lijst_van_vragen:
            lijst_van_vragen.remove('0')

        vragen2 = open("inleveropdracht_1_accounts.txt", "rt")

        data = vragen2.read()
        data = data.replace(
            self.naam + "|" + str(self.score) + "|" + str(self.aantal_gespeeld) + "|" + str(self.gemaakte_vragen),
            self.naam + "|" + str(self.score) + "|" + str(self.aantal_gespeeld) + "|" + str(lijst_van_vragen))
        vragen.close()

        vragen = open("inleveropdracht_1_accounts.txt", "wt")
        vragen.write(data)
        vragen.close()

        self.gemaakte_vragen = lijst_van_vragen

    # functie om de gebruikersnaam en score van een gebruiker te weergeven,
    # wordt gebruikt bij de menu optie om gegevens te bekijken en aan te passen
    def display_details(self):
        print("\nJe gebruikersnaam is " + str(self.naam) +
              "\nJe huidige score is " + str(self.score) +
              "\nJe hebt " + str(self.aantal_gespeeld) + " keer een quiz gespeeld" +
              "\nen je hebt de volgende vragen gemaakt: " + str(self.gemaakte_vragen) + "\n")

    # functie om de username op te vragen en te returnen.
    def get_username(self):
        return self.naam

    def get_score(self):
        return self.score

    def get_aantal(self):
        return self.aantal_gespeeld

    def get_gemaaktevragen(self):
        return self.gemaakte_vragen

    def reset_all(self):
        gegevens = open("inleveropdracht_1_accounts.txt", "rt")
        data = gegevens.read()
        data = data.replace(
            self.naam + "|" + str(self.score) + "|" + str(self.aantal_gespeeld) + "|" + str(self.gemaakte_vragen),
            self.naam + "|" + str(0) + "|" + str(0) + "|" + str(0))
        gegevens.close()

        gegevens = open("inleveropdracht_1_accounts.txt", "wt")
        gegevens.write(data)
        gegevens.close()

        self.score = 0
        self.aantal_gespeeld = 0
        self.gemaakte_vragen = 0

    # functie om in te loggen, alle gebruikersnamen worden in een list
    # gestopt en vergeleken met de waarde die ingevoerd is. Als de waarde gelijk is,
    # wordt ingelogd met dat account. Anders wordt een nieuw account aangemaakt
    # en wordt daarmee ingelogd
    def login(self, naam):
        accounts = open("inleveropdracht_1_accounts.txt", "r")
        lijst_met_namen = []
        lijst_met_gebruikers = []

        for x in accounts:
            lijst_met_gebruikers.append(x.split("|"))

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
                    aantal_gespeeld2 = p[2]
                    gemaakte_vragen2 = p[3]

                    self.set_score(score_gebruiker)
                    self.gemaakte_vragen = gemaakte_vragen2
                    self.aantal_gespeeld = aantal_gespeeld2

            except IndexError:
                pass

        if naam in lijst_met_namen:
            print("\nHoi, " + str(naam) + ". Welkom terug!\nje score is " + score_gebruiker + "\n")
        else:
            namen2 = open("inleveropdracht_1_accounts.txt", "a")
            namen2.write("\n" + naam + "|" + str(self.score) + "|" + "0" + "|" + "0")
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

        while flag:
            vraagtitel = input("Wat is je vraag? (typ n om terug te keren naar het menu)")
            if vraagtitel == "":
                print("Je hebt een lege waarde ingevuld")
                flag = True
            elif vraagtitel == "n":
                menu()
            else:
                flag = False
        flag = True
        while flag:
            antwoordvraag = input("Wat is het antwoord bij de vraag? (typ n om terug te keren naar het menu)")
            if antwoordvraag == "":
                print("Je hebt een lege waarde ingevuld")
                flag = True
            elif antwoordvraag == "n":
                menu()
            else:
                flag = False

        print("De volgende thema's bestaan al")
        for thema in beschikbare_themas:
            print(thema)
        bestaand_thema_kiezen = input("Wil je hier een of meerdere uit kiezen? (y/n)")
        if bestaand_thema_kiezen == 'y':
            for thema in beschikbare_themas:
                input_bestaand_thema_toevoegen = input("Wil je thema " + thema + " toevoegen? (y/n)")
                if input_bestaand_thema_toevoegen == "y":
                    lijst_van_themas.append(thema)
        else:
            pass

        flag = True
        while flag:
            themas_toevoegen = input("Wil je zelf nog themas toevoegen? (enter voor nee, thema intypen voor ja)")
            if themas_toevoegen == "":
                flag = False
            else:
                lijst_van_themas.append(themas_toevoegen)
                themas = open("inleveropdracht_1_themas.txt", "a")
                themas.write("\n" + themas_toevoegen)

        type = input("Wat voor type vraag is het? (open/gesloten?)")

        self.set_gemaakte_vragen(str(vraagtitel))
        new_question = LosseVraag(vraagtitel, type, lijst_van_themas, antwoordvraag, self)
        new_question.opslaan_vraag()
        print("Je hebt succesvol een vraag aangemaakt!")

class LosseVraag:
    # om een object te kunnen maken van LosseVraag
    def __init__(self, titel, type, thema, antwoord, bedenker):
        self.titel = titel
        self.type = type
        self.thema = thema
        self.antwoord = antwoord
        self.bedenker = bedenker

    # functies om de titel, type etc. aan de passen naar de ingevoerde waarde
    # past tot nu toe alles aan waar de waarde van self.titel(type/thema etc) in voorkomt
    # kan voor problemen zorgen
    def set_titel(self, newtitel):
        titels = open("inleveropdracht_1_lossevragen.txt", "rt")
        data = titels.read()
        data = data.replace(self.titel, newtitel)
        titels.close()

        titels = open("inleveropdracht_1_lossevragen.txt", "wt")
        titels.write(data)
        titels.close()

        self.titel = newtitel

    def set_type(self, newtype):
        types = open("inleveropdracht_1_lossevragen.txt", "rt")
        data = types.read()
        data = data.replace(self.type, newtype)
        types.close()

        types = open("inleveropdracht_1_lossevragen.txt", "wt")
        types.write(data)
        types.close()
        self.type = newtype

    def set_thema(self, newthema):
        themas = open("inleveropdracht_1_lossevragen.txt", "rt")
        data = themas.read()
        data = data.replace(self.thema, newthema)
        themas.close()

        themas = open("inleveropdracht_1_lossevragen.txt", "wt")
        themas.write(data)
        themas.close()
        self.thema = newthema

    def set_antwoord(self, newantwoord):
        antwoorden = open("inleveropdracht_1_lossevragen.txt", "rt")
        data = antwoorden.read()
        data = data.replace(self.antwoord, newantwoord)
        antwoorden.close()

        antwoorden = open("inleveropdracht_1_lossevragen.txt", "wt")
        antwoorden.write(data)
        antwoorden.close()
        self.antwoord = newantwoord

    # einde aanpasfuncties

    # functie om een nieuwe vraag op te slaan in de .txt file daarvoor
    def opslaan_vraag(self):
        username = self.bedenker.get_username()
        lossevragen = open("inleveropdracht_1_lossevragen.txt", "a")
        lossevragen.write("\n" + str(self.titel) + "|" + str(self.type) + "|" + str(self.thema) + "|"
                          + str(self.antwoord) + "|" + str(username))
        lossevragen.close()

    # functie om de gekozen vraag te laten zien in quiz vorm. De gebruiker typt het antwoord in
    # (tot nu toe alleen maar voor open vragen) en bij een correct antwoord worden
    # 10 punten toegekend
    # De gebruiker kan op elk gewenst moment de quiz staken door n te typen
    def display_vraag(self):
        print("De vraag is bedacht door " + str(self.bedenker))
        print(str(self.titel))
        givenanswer = input("Wat is het antwoord? (Typ 'n' om de quiz te stoppen)")
        if givenanswer == self.antwoord:
            print("Dat is correct!")

            the_user.set_score(10)
            print("Je score is nu " + str(the_user.score))
        elif givenanswer == 'n':
            print("\n Je hebt ervoor gekozen om de quiz te stoppen, je keert nu terug naar het menu \n")
            menu()
        else:
            print("Helaas, dat klopt niet! Het antwoord was: " + self.antwoord)

class Quiz:
    # om een object te kunnen maken van de klasse Quiz
    def __init__(self, titel, themas):
        self.titel = titel
        self.themas = themas

    # de vragen van de gekozen quiz (zie volgende methode) worden opgehaald
    # een nieuw object wordt gemaakt en de functie display wordt uitgevoerd.
    def play_quiz(self, gekozen_quiz, hoeveel_vragen):
        vragen = open("inleveropdracht_1_lossevragen.txt", "rt")
        lijst_van_vragen = []
        lijst_van_uiteindelijke_vragen = []

        for vraag in vragen:
            try:
                lijst_van_vragen.append(vraag.split("|"))
            except IndexError:
                pass

        for x in lijst_van_vragen:
            try:
                if gekozen_quiz in x[2]:
                    lijst_van_uiteindelijke_vragen.append(x)
            except IndexError:
                pass
        counter = 0

        #vragen moeten nog random worden
        for x in lijst_van_uiteindelijke_vragen:
            if counter < int(hoeveel_vragen):
                try:
                    de_vraag = LosseVraag(x[0], x[1], x[2], x[3], x[4])
                    de_vraag.display_vraag()
                    counter += 1

                except IndexError:
                    pass
        the_user.set_aantal_gespeeld(1)
    def choose_quiz(self):
        flag = True
        while flag:
            vragen = open("inleveropdracht_1_lossevragen.txt", "rt")
            lijst_van_vragen = []
            lijst_van_themas = []
            volle_lijst_themas = []

            for vraag in vragen:
                lijst_van_vragen.append(vraag.split('|'))

            #Zorgt ervoor dat de verschillende thema's van een vraag eruit gehaald kunnen worden
            try:
                for thema in lijst_van_vragen:
                    for x in ['[', ']', '\'', '\"', ' ']:
                        thema[2] = thema[2].replace(x, '')
                        thema[2] = thema[2].replace(', ', '|')

                    if '|' in thema[2]:
                        split = thema[2].split('|')
                        for x in split:
                            volle_lijst_themas.append(x)
                    else:
                        volle_lijst_themas.append(thema[2])

                ##zorgt ervoor dat alleen thema's worden weergeven waar meer dan 5 vragen van zijn
                for x in volle_lijst_themas:
                    if volle_lijst_themas.count(x) >= 5 and x not in lijst_van_themas:
                        lijst_van_themas.append(x)

            except IndexError:
                print("fout1")
                pass

            print("Je hebt keuze uit de volgende thema's: ")
            for option in lijst_van_themas:
                print(option)
            for option in lijst_van_themas:
                keuze = input("Wil je een quiz met het thema " + option + " spelen? (y/n)")
                if keuze == "y":
                    print("je hebt gekozen om " + option + " te spelen")
                    gekozen_thema = option

                    ### vraagt het aantal vragen dat de gebruiker wil spelen, en geeft de nodige foutmeldingen
                    ### wanneer er iets aan de input niet klopt
                    flag = True
                    while flag:
                        try:
                            aantal_vragen = input(
                            "Hoeveel vragen wil je spelen? Max " + str(volle_lijst_themas.count(gekozen_thema)))

                            if int(aantal_vragen) > volle_lijst_themas.count(gekozen_thema):
                                print("Je hebt meer vragen ingevuld dan er zijn.")
                                flag = True
                            elif int(aantal_vragen) == 0:
                                print("Je hebt 0 ingevuld.")
                                flag = True
                            else:
                                self.play_quiz(gekozen_thema, aantal_vragen)
                                flag = False
                        except TypeError:
                            print("Je input klopte niet helemaal, probeer het nog een keer")
                            flag = True
                        except ValueError:
                            print("Je input klopte niet helemaal, probeer het nog een keer")
                            flag = True
                    continue
                else:
                    continue
            print("\n De quiz is voorbij of je hebt gekozen geen quiz te spelen. Je wordt terug naar het menu gebracht \n")
            break

# functie die het gehele programma afspeeld vanaf het inlogscherm
def start_program():
    print("\nWelkom bij de quizz applicatie! \n")
    inlognaam = input("Wat is je gebruikersnaam?")
    global the_user
    the_user = Gebruiker(inlognaam, 0, 0, 0)
    the_user.login(inlognaam)
    menu()


# de functie voor het menu, wordt aangeroepen na het inloggen, en wanneer
# terugverwezen wordt naar het menu
def menu():
    # zorgt dat het menu steeds opnieuw aangeboden wordt
    flag = True

    while flag:
        menu_keuze = input("Typ 'g' om je profielgegevens te bekijken en aan te passen\n"
                           "Typ 'l' om een losse vraag aan te maken \n"
                           "Typ 's' om een quiz te spelen\n"
                           "Typ 'a' om een vraag aan te passen\n"
                           "Typ 'u' om uit te loggen\n"
                           "Typ 'e' om de applicatie af te sluiten")
        # serie if en elifs om naar de gewenste onderdelen van de applicatie te leiden
        if menu_keuze == 'g':
            the_user.display_details()
            actie_user = input("Wat wil je doen?\n"
                               "Typ '1' om je gebruikersnaam aan te passen\n"
                               "Typ '2' om je gegevens te resetten\n"
                               "Typ iets anders om terug naar het menu te keren\n" )
            if actie_user == "1":
                nieuwewaarde = input("wat is je nieuwe gebruikersnaam?")
                the_user.set_gebruikersnaam(nieuwewaarde)
            elif actie_user == "2":
                the_user.reset_all()
                print("Je gegevens zijn gereset!")
            else:
                print("\nJe wordt terug naar het menu gebracht.\n")
                pass
        elif menu_keuze == 'l':
            print("Je gaat nu een losse vraag aanmaken")
            the_user.maak_losse_vraag()
            pass
        elif menu_keuze == 's':
            print("Welke quiz wil je spelen?")
            the_quiz = Quiz("", "")
            the_quiz.choose_quiz()
            pass
        elif menu_keuze == 'a':
            lossevragen = open("inleveropdracht_1_lossevragen.txt", "r")
            lijst_met_vragen = []
            lijst_met_vragen_nieuw = []

            for vraag in lossevragen:
                lijst_met_vragen.append(vraag.split('|'))

            # een extra lijst om de vraagtitels op te slaan van de vragen die de gebruiker gemaakt heeft
            # zo kan een overzicht worden getoont waaruit de gebruiker kan kiezen
            for vraag in lijst_met_vragen:
                if vraag[4] == the_user.naam or vraag[4] == the_user.naam + "\n":
                    lijst_met_vragen_nieuw.append(vraag[0])

            ###### Functie past tot nu toe alles in het document aan dat overeenkomt
            ###### met de oude waardes. (als een antwoord van ja naar nee wordt aangepast,
            ###### worden ze allemaal aangepast.
            print("\nJe kunt alleen vragen aanpassen die je zelf gemaakt hebt. Dit zijn de volgende vragen: \n")
            for x in lijst_met_vragen_nieuw:
                print(x)

            for vraag in lijst_met_vragen:
                if vraag[4] == the_user.naam or vraag[4] == the_user.naam + "\n":
                    answer = input("\nTyp 'y' om de vraag " + vraag[0] + " aan te passen. Typ 'm' om terug naar het menu te gaan")
                    if answer == 'y':
                        placeholder = LosseVraag(vraag[0], vraag[1], vraag[2], vraag[3], vraag[4])
                        nieuwe_titel = input("wat is de nieuwe vraag? (druk op enter om over te slaan)")
                        if nieuwe_titel != "":
                            placeholder.set_titel(nieuwe_titel)
                        nieuwe_type = input("wat is het nieuwe type? (druk op enter om over te slaan)")
                        if nieuwe_type != "":
                            placeholder.set_type(nieuwe_type)
                        nieuwe_thema = input("wat is het nieuwe thema? (druk op enter om over te slaan)")
                        if nieuwe_thema != "":
                            placeholder.set_thema(nieuwe_thema)
                        nieuwe_antwoord = input("wat is het nieuwe antwoord? (druk op enter om over te slaan)")
                        if nieuwe_antwoord != "":
                            placeholder.set_antwoord(nieuwe_antwoord)
                        pass
                    elif answer == 'm':
                        print("\n je wordt terug naar het menu gebracht \n")
                        menu()
                    else:
                        pass
        elif menu_keuze == 'u':
            print("Je wordt nu uitgelogd")
            the_user.logout()
        elif menu_keuze == 'e':
            print("De applicatie wordt nu afgesloten.")
            exit()
        else:
            print("Je input klopte niet helemaal, probeer het nog een keer")
            flag = True

start_program()
