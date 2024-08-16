from weapon import create_weapon

class Player:
    def __init__(self, name, health=100):
        self.health = health
        self.items = []
        #edited line below
        self.weapon = create_weapon("fists")
        self.name = name

    def reduce_health(self, hp):
        self.health -= hp

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
        print(f"{self.name}'s health: {self.health}.'")
        return self.health > 0
            