def start_program():
    naam = input("Wat is je naam?")
    namen = open("oefening4_namen.txt", "r")
    lijst_met_namen = []

    for x in namen:
        lijst_met_namen.append(x.split())

    if naam in lijst_met_namen[0]:
        print("hoi, " + naam)
    else:
        namen2 = open("oefening4_namen.txt", "a")
        namen2.write(" " + naam)
        namen.close()
        print("Welkom, " + naam + ". er is een nieuw account voor je aangemaakt")
    flag = True

    while flag:
        input_value = input(
            "Typ 'a' voor optie a, typ 'b' voor optie b. Typ 't' om terug te gaan. Typ 's' om te stoppen.")
        if input_value == "a":
            print("Dit is optie a")
            flag = False
        elif input_value == "b":
            print("Dit is optie b")
            flag = False
        elif input_value == "s":
            exit()
            flag = False
        elif input_value == "t":
            start_program()
            flag = False
        else:
            print("je hebt niet voor een van de opties gekozen!")
            flag = True

start_program()


