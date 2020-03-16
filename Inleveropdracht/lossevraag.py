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
    def display_vraag(self):
        print("De vraag is bedacht door " + str(self.bedenker))
        print(str(self.titel))
        givenanswer = input("Wat is het antwoord?")
        if givenanswer == self.antwoord:
            print("Dat is correct!")
            the_user.set_score(10)
            print("Je score is nu " + str(the_user.score))
        else:
            print("Helaas, dat klopt niet! Het antwoord was: " + self.antwoord)