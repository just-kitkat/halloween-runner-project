class Player:
    def __init__(self, health=100):
        self.health = health
        self.items = []

    def reduce_health(hp):
        self.health -= hp

    def fight_monster(self, monster) -> bool:
        turn = "attack"
        while self.health > 0 and monster.get_health() > 0:
            if turn == attack:
                monster.player_attack_monster()
            else:
                monster.monster_attack_player()
            turn = "defend" if turn == "attack" else attack
            