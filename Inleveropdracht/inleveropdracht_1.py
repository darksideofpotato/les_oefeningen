###### Er is nog niet gecontroleerd op mogelijkheid om van elk punt in de applicatie
###### de applicatie af te sluiten of uit te loggen, dit kan op bepaalde punten nog ontbreken

# counter om het aantal vragen per thema te kunnen tellen
from collections import Counter

#classes gebruiker, quiz en lossevraag
from gebruiker import *
from quiz import *
from lossevraag import *

# functie die het gehele programma afspeeld vanaf het inlogscherm
def start_program():
    print("Welkom bij de quizz applicatie!")
    inlognaam = input("Wat is je gebruikersnaam?")
    global the_user
    the_user = Gebruiker(inlognaam, 0)
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
            aanpassen = input("wil je je gebruikersnaam aanpassen? y/n")
            if aanpassen == "y":
                nieuwewaarde = input("wat is je nieuwe gebruikersnaam?")
                the_user.set_gebruikersnaam(nieuwewaarde)
            else:
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

            for vraag in lossevragen:
                lijst_met_vragen.append(vraag.split('|'))

            ###### Functie past tot nu toe alles in het document aan dat overeenkomt
            ###### met de oude waardes. (als een antwoord van ja naar nee wordt aangepast,
            ###### worden ze allemaal aangepast.

            for vraag in lijst_met_vragen:
                answer = input("Typ 'y' om de vraag " + vraag[0] + " aan te passen")
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
