"""combat.py

Base classes and helper functions for combat implementation.
"""


class Combatant:
    """Superclass for all entities engaging in combat."""
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None
        self.armor = None

    def get_health(self):
        return self.health

    def reduce_health(self, hp):
        # Health is allowed to drop below 0.
        self.health -= hp

    def add_health(self, hp):
        # No upper limit to combatant health.
        self.health += hp

    def is_dead(self) -> bool:
        return self.health <= 0

    def damage(self) -> int:
        """Damage dealt to enemy"""
        return self.weapon.damage if self.weapon else 0

    def defense(self) -> int:
        """Damage reduction"""
        return self.armor.protection if self.armor else 0
