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
