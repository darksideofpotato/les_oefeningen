class Gebruiker:
    def __init__(self, naam, score):
        self.naam = naam
        self.score = score

    def set_gebruikersnaam(self, gebruikersnaam):
        self.naam = gebruikersnaam
        #past het nog niet aan in de database

    def set_score(self, ing_score):
        self.score = ing_score

    def display_details(self):
        print("Je gebruikersnaam is " + str(self.naam) +
              "\nJe huidige score is " + self.score)

    def add_user(self):
        pass
    #hier komt nog de invulling van de functie

    def login(self, naam):
        accounts = open("inleveropdracht_1_accounts.txt", "r")
        lijst_met_namen = []
        lijst_met_gebruikers = []

        for x in accounts:
            lijst_met_gebruikers.append(x.split())

        for y in  lijst_met_gebruikers:
            lijst_met_namen.append(y[0])

        for p in lijst_met_gebruikers:
            if p[0] == naam:
                score_gebruiker = p[1]
                self.set_score(score_gebruiker)

        if naam in  lijst_met_namen:
            print("hoi, " + str(naam) + " je score is " + score_gebruiker)
        else:
            namen2 = open("inleveropdracht_1_accounts.txt", "a")
            namen2.write("\n" + naam + " " + str(self.score))
            accounts.close()
            print("Welkom, " + naam + ". er is een nieuw account voor je aangemaakt")
    def logout(self):
        pass
    #hier komt nog de invulling van de functie

class Quiz:
    def __init__(self, titel, themas):
        self.titel = titel
        self.themas = themas

    def set_quiztitel(self, newtitel):
        self.titel = newtitel

    def set_quizthemas(self, newthema):
        self.themas = newthema

    def play_quiz(self):
        pass

class LosseVraag:
    def __init__(self, titel, type, thema, antwoord):
        self.titel = titel
        self.type = type
        self.thema = thema
        self.antwoord = antwoord

    def set_titel(self, newtitel):
        self.titel = newtitel

    def set_type(self, newtype):
        self.titel = newtype

    def set_thema(self, newthema):
        self.thema = newthema

    def set_antwoord(self, newantwoord):
        self.antwoord = newantwoord

    def display_vraag(self):
        print("Vraag: " + self.titel)
        givenanswer = input("Wat is het antwoord?")
        if givenanswer == self.antwoord:
            print("Dat is correct!")
        else:
            print("Helaas, dat klopt niet! Het antwoord was: " + self.antwoord)

def start_program():
    print("Welkom bij de quizz applicatie!")
    inlognaam = input("Wat is je gebruikersnaam?")
    the_user = Gebruiker(inlognaam, 0)
    the_user.login(inlognaam)


    flag = True

    while flag:
        menu_keuze = input("Typ 'g' om je profielgegevens te bekijken en aan te passen\n"
                           "Typ 'q' om een quiz aan te maken \n"
                           "Typ 'l' om een losse vraag aan te maken \n"
                           "Typ 's' om een quiz te spelen\n"
                           "Typ 'u' om uit te loggen\n"
                           "Typ 'e' om de applicatie af te sluiten")
        if menu_keuze == 'g':
            the_user.display_details()
            aanpassen = input("wil je je gebruikersnaam aanpassen? y/n")
            if aanpassen == "y":
                nieuwewaarde = input("wat is je nieuwe gebruikersnaam?")
                the_user.set_gebruikersnaam(nieuwewaarde)
            else:
                pass
        elif menu_keuze == 'q':
            print("Je gaat nu een quiz maken")
            pass
        elif menu_keuze == 'l':
            print("Je gaat nu een losse vraag aanmaken")
            maak_losse_vraag()
            pass
        elif menu_keuze == 's':
            print("Welke quiz wil je spelen?")
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

def maak_losse_vraag():
    vraagtitel = input("Wat is de titel van je vraag?")
    antwoordvraag = input("Wat is het antwoord bij de vraag?")
    thema = input("Wat is het thema van de vraag?")
    type = input("Wat voor type vraag is het?")

    new_question = LosseVraag(vraagtitel, type, thema, antwoordvraag)
    new_question.display_vraag()

start_program()

