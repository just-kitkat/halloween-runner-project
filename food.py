import random

"""class Food:
    def __init__(self,data):
        self.name = data["name"]
        self.healing = data["health"]

    def use(self,player):
        #per turn the player takes how much he heals, its healing over time, decreases by 1 per turn until 0
        player.add_health(self.healing)"""

food_data = {
    "apple":{
        "name":"Apple",
        "health":3
    },
    "orange":{
        "name":"Orange",
        "health":3
    },
    "durian":{
        "name":"Mao Shan Wang Durian",
        "health":9
    },
    "chocolate":{
        "name":"Ferrero Rocher",
        "health":6
    },
    "mala":{
        "name":"Mala",
        "health":6
    },
}

def all_food():
    return list(food_data.keys())

def use(player):
    food = food_data[random.choice(all_food())]
    print(f"You found a {food["name"]} and ate it, gaining {food["health"]} health!")
    player.add_health(food["health"])
    print(f"Your health: {player.get_health()}")