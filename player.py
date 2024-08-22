import time
from weapon import create_weapon, create_random_weapon
from armour import create_armour, create_random_armour

class Player:
    def __init__(self,name, health=100):
        self.health = health
        self.items = []
        #edited line below
        self.weapon = create_weapon("fists")
        self.name = name
        self.armor = create_armour("white tshirt")

    def get_health(self):
        return self.health
    
    def reduce_health(self, hp):
        self.health -= hp

    def add_health(self, hp):
        self.health += hp

    def fight_monster(self, monster):
        if monster is None:
            print("There are no monsters in this room!")
            return None
        turn = "attack"
        while self.health > 0 and monster.get_health() > 0:
            if turn == "attack":
                monster.player_attack_monster(self)
            else:
                monster.monster_attack_player(self)
            turn = "defend" if turn == "attack" else "attack"
            input("Press enter to continue: ")
            print()
        return self.health > 0

    def display_weapon_armor_options(self):
        weapon = create_random_weapon()
        print("You found a weapon in the room!")
        time.sleep(1)
        print(f"""
Weapon: {weapon.name}
Damage: {weapon.damage}
Accuracy: {weapon.accuracy}

{weapon.description}
""")
        choice = input("""Do you want to pick up this weapon?
Enter 'pick' to pick up the weapon.
Enter any other string to leave the weapon.
Choice: """)
        if choice == "pick":
            print("You have picked up the weapon")
            self.weapon = weapon
        else:
            print("You have ditched the weapon.")


        armor = create_random_armour()
        print("\nYou found a piece of armour in the room!")
        time.sleep(1)
        print(f"""
Armor: {armor.name}
Protection: {armor.protection}

{armor.description}
""")
        choice = input("""Do you want to pick up this armour?
Enter 'pick' to pick up the armour.
Enter any other string to leave the armour.
Choice: """)
        if choice == "pick":
            print("You have picked up the armour")
            self.armor = armor
        else:
            print("You have ditched the armour.")

            