"""battle.py

Functions and classes that encapsulate battle rules for the game.
"""
import math
import random

import monster
import player


class StrikeResult:
    def __init__(
            self,
            attacker_name: str,
            attacker_weapon: str,
            defender_name: str,
            defender_weapon: str,
            hit: bool,
            damage: int,
            reduction: int,
    ):
        self.attacker_name = attacker_name
        self.attacker_weapon = attacker_weapon
        self.defender_name = defender_name
        self.defender_weapon = defender_weapon
        self.hit = hit
        self.damage = damage
        self.reduction = reduction


class Battle: 
    def __init__(self, fighter1: player.Player, fighter2: monster.Monster):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def is_ended(self) -> bool:
        """Battle ends when either fighter dies."""
        return self.fighter1.is_dead() or self.fighter2.is_dead()

    def strike(self, attacker, defender) -> StrikeResult:
        """A single blow by an attacker to a defender."""
        if random.randint(1, 100) > attacker.accuracy():
            #attack missed
            return StrikeResult(
                attacker_name=attacker.name,
                attacker_weapon=attacker.weapon.name,
                defender_name=defender.name,
                defender_weapon=defender.weapon.name,
                hit=False,
                damage=0,
                reduction=0,
            )
        #attack hit
        damage = attacker.damage()
        if damage == 1:
            reduction = 0
        else:
            reduction = math.ceil(
                damage * defender.defense() / 100
            )
        return StrikeResult(
            attacker_name=attacker.name,
            attacker_weapon=attacker.weapon.name,
            defender_name=defender.name,
            defender_weapon=defender.weapon.name,
            hit=True,
            damage=damage,
            reduction=reduction,
        )

    def exchange(self) -> list[StrikeResult]:
        """A single exchange of attacks between the two fighters.
        Returns the result of the exchange, as a list of StrikeResults.
        """
        results = []
        # Fighter 1 goes first
        result = self.strike(self.fighter1, self.fighter2)
        if result.hit:
            self.fighter2.reduce_health(result.damage - result.reduction)
        results.append(result)
        if self.is_ended():
            return results

        # Fighter2 goes next
        result = self.strike(self.fighter2, self.fighter1)
        if result.hit:
            self.fighter1.reduce_health(result.damage - result.reduction)
        results.append(result)
        return results
