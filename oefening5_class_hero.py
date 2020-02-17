class Hero:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def aanval(self):
        print(self.name + " heeft een aanval gedaan, dit heeft " + str(self.attack) + " damage gedaan. "
              + self.name + " heeft nog " + str(health_value) + " health over.")

naam = input("Wat is je naam?")
attack_value = input("Wat is de attack value?")
health_value = input("Wat is de health?")

new_Hero = Hero(naam, attack_value, health_value)

actie = input("Vul 'a' in om aan te vallen")
if actie == 'a':
    new_Hero.aanval()
else:
    print("Je hebt gekozen om geen aanval te doen.")