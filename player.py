from combat import Combatant
from weapon import create_weapon, create_random_weapon
from armour import create_armour, create_random_armour


class Player(Combatant):

    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.items = []
        #edited line below
        self.weapon = create_weapon("fists")
        self.armor = create_armour("white tshirt")
