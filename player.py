from weapon import create_weapon
from armour import create_armour

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
        return self.health > 0
            