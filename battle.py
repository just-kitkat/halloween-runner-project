"""battle.py

Functions and classes that encapsulate battle rules for the game.
"""
import math
import random

import monster
import player
import weapon


class Battle: 
    def __init__(self, fighter1: player.Player, fighter2: monster.Monster):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def strike(self, attacker, defender):
        """A single blow by an attacker to a defender."""
        if random.randint(1, 100) > attacker.accuracy():
            #attack missed
            return [False, 0]
        #attack hit
        damage = attacker.damage()
        if damage == 1:
            reduction = 0
            return [True, damage, 0]
        else:
            reduction = math.ceil(
                damage * defender.defense() / 100
            )
            return [True, damage, reduction]
