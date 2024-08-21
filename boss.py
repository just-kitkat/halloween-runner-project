from monster import create_boss

def boss_fight(player):
    print("BOSS_APPEARANCE_MESSAGES HERE (can add time.sleep()")
    boss = create_boss()

    win = player.fight_monster(boss)

    if win:
        print("You have cleared the dungeon and defeated the monster!")
        print("Congratulations!")
    else:
        print("You have failed... maybe try again when you get stronger...")