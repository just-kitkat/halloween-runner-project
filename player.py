from weapon import create_weapon, create_random_weapon
from armour import create_armour, create_random_armour


class Player:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.items = []
        #edited line below
        self.weapon = create_weapon("fists")
        self.armor = create_armour("white tshirt")

    def get_health(self):
        return self.health

    def reduce_health(self, hp):
        self.health -= hp

    def add_health(self, hp):
        self.health += hp

    def is_dead(self) -> bool:
        return self.health <= 0

    def damage(self) -> int:
        """Player's damage dealt to enemy"""
        return self.weapon.damage if self.weapon else 0

    def defense(self) -> int:
        """Player's damage reduction"""
        return self.armor.protection if self.armor else 0

