"""battle.py

Functions and classes that encapsulate battle rules for the game.
"""
import monster
import player
import weapon


class Battle: 
    def __init__(self, fighter1: player.Player, fighter2: monster.Monster):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def strike(self, attacker, defender):
        """A single blow by an attacker to a defender."""
        lst = attacker.weapon.attack(defender, defender.armor.protection)
        bool = lst[0]
        if bool:
            print(
                f"{attacker.name} attacked {defender.name} with \"{attacker.weapon.name}\", dealing {lst[1]} damage"
            )
            if lst[2] != 0:
                print(f"{defender.name}'s armour protected you from {lst[2]} damage!")
        else:
            print(f"{attacker.name}\'s attack missed!")
