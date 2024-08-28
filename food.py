import random
import time

import data

"""class Food:
    def __init__(self,data):
        self.name = data["name"]
        self.healing = data["health"]

    def use(self,player):
        #per turn the player takes how much he heals, its healing over time, decreases by 1 per turn until 0
        player.add_health(self.healing)"""

food_data = data.load("food.json")

class Food:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def info(self) -> str:
        return ""

def all_food():
    return list(food_data.keys())

def create_food(data: dict) -> Food:
    return Food(data["name"], data["health"])

def random_food() -> Food:
    return create_food(random.choice(all_food()))

def heal(player):
    food = random_food()
    print(f"You found a {food.name} and ate it, gaining {food.health} health!")
    player.add_health(food.health)
    print(f"Your health: {player.get_health()}")
    time.sleep(3)