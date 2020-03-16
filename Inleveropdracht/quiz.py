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

    def choose_quiz(self):
        flag = True
        while flag:
            vragen = open("inleveropdracht_1_lossevragen.txt", "rt")
            lijst_van_vragen = []
            lijst_van_themas = []
            volle_lijst_themas = []

            for vraag in vragen:
                lijst_van_vragen.append(vraag.split('|'))

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
                    break
                else:
                    pass
            aantal_vragen = input("Hoeveel vragen wil je spelen? Max " + str(volle_lijst_themas.count(gekozen_thema)))
            self.play_quiz(gekozen_thema, aantal_vragen)

            ##Lange loop + start ook quiz bij n