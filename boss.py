from monster import create_boss
from boss_msg import boss_entry
import time


def boss_fight(player):
    for msg in boss_entry["enter_room"]:
        print(msg)
        time.sleep(3)

    boss = create_boss()
    win = player.fight_monster(boss)

    key = "player_win" if win else "player_lose"
    for msg in boss_entry[key]:
        print(msg)
        time.sleep(5)
