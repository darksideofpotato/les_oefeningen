import random


class Hero:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
        self.health = 100

    def setHealth(self, new_health):
        self.health = new_health

    def setAttack(self, new_attack):
        self.attack = new_attack

    def aanval(self, enemy_name, enemy_health, hero_or_enemy):
        random_attack = self.attack + random.randint(5, 10)
        enemy_health_new = enemy_health - random_attack
        if hero_or_enemy == "hero":
            enemy_hero.setHealth(enemy_health_new)
        elif hero_or_enemy == "enemy":
            new_Hero.setHealth(enemy_health_new)

        print(self.name + " heeft een aanval gedaan, dit heeft " + str(random_attack) + " damage gedaan. "
        + str(enemy_name) + " heeft nog " + str(enemy_health_new) + " health over.")

class Item:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def upgrade(self):
        new_attack = random.randint(1, 10)
        new_defense = random.randint(1, 10)
        new_Hero.attack += new_attack
        new_Hero.health += new_defense

def start_spel():
    print("Welkom bij dit spel! Je gaat een eigen karakter aanmaken die tegen anderen vecht.")
    chosen_name = input("Wat is de naam van de karakter?")
    global new_Hero
    new_Hero = Hero(chosen_name, 30)

    print("Je nieuwe hero is aangemaakt! De naam is " + chosen_name + " de basis attack van je hero is " + str(new_Hero.attack) +
          " en de health is " + str(new_Hero.health) + " . Je hebt nu de keuze om een item uit te kiezen. Je hebt keuze uit de volgende: ")

    choice_of_weapon = input("Typ '1' voor maliënkolder die 20 defense geeft en -10 attack \n Typ '2' voor stalen armor die 30 defense geeft en -20 attack \n"
                             "Typ '3' voor dolk die 20 attack geeft en -10 defense \n Typ '4' voor zwaard die 30 attack geeft en -20 defense.")

    if choice_of_weapon == "1":
        item_naam = "malienkolder"
        item_attack = -10
        item_defense = 20
    elif choice_of_weapon == "2":
        item_naam = "stalen armor"
        item_attack = -20
        item_defense = 30
    elif choice_of_weapon == "3":
        item_naam = "dolk"
        item_attack = 20
        item_defense = -10
    elif choice_of_weapon == "4":
        item_naam = "zwaard"
        item_attack = 30
        item_defense = -20
    else:
        pass

    global gekozen_wapen
    gekozen_wapen = Item(item_naam, item_attack, item_defense)
    new_Hero.setHealth(new_Hero.health + gekozen_wapen.defense)
    new_Hero.setAttack(new_Hero.attack + gekozen_wapen.attack)
    ##########################
    next_action = input("Wil je het spel beginnen? (y/n)")
    if next_action == "y":
        encounter_enemy()
    else:
        print("He hebt ervoor gekozen het spel niet te spelen, het wordt nu afgesloten")
        exit()


def encounter_enemy():
    global enemy_hero
    enemy_hero = Hero("Orc", 20)

    print("Oei, je bent een enemy tegen gekomen, " + enemy_hero.name + " met " + str(enemy_hero.attack) + " attack en "
          + str(enemy_hero.health) + " health. Wil je de enemy aanvallen of opgeven?")
    aangaan = input("a = aanvallen, o = opgeven")
    if aangaan == "o":
        "Je hebt ervoor gekozen op te geven, het spel wordt afgesloten!"
        exit()
    elif aangaan == "a":
        print("je hebt besloten om aan te vallen!")
        doorgaan = True
        while doorgaan:
            enemy_health = enemy_hero.health
            hero_health = new_Hero.health

            if enemy_health <= 0:
                print("Hoera! de " + enemy_hero.name + " is verslagen en je hebt gewonnen!")
                doorgaan = False
            elif hero_health <= 0:
                print("Helaas, "+ new_Hero.name + " is verslagen en je hebt verloren!")
                doorgaan = False
            else:
                actie = input("Vul 'a' in om een attack te doen, 'u' om je item te upgraden")
                if actie == 'a':
                    new_Hero.aanval(enemy_hero.name, enemy_health, "hero")
                    ###Check of dood is
                    enemy_hero.aanval(new_Hero.name, hero_health, "enemy")
                elif actie == 'u':
                    gekozen_wapen.upgrade()
                    print("Je hebt ervoor gekozen te item te upgraden. Je huidige stats zijn nu: \n"
                          "health = " + str(new_Hero.health) + " attack = " + str(new_Hero.attack))
                    enemy_hero.aanval(new_Hero.name, hero_health, "enemy")
                else:
                    print("Je hebt opgegeven en bent dus verslagen!")
                    exit()

start_spel()