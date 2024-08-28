import room
import introduction
import player
import time
from boss import boss_fight
from food import heal

TOTAL_ROOMS = 5


class Game:

    def __init__(self, name):
        self.rooms_cleared = 0
        self.dungeon = room.Dungeon()
        self.player = player.Player(name)

    def sleep(self):
        return time.sleep(1.5)


def intro():
    start = introduction.display_startingmsg()
    return start

def main():
    # Continuation of storyline from blackout
    print("You wake up and find youself in a mysterious place...\n")
    time.sleep(5)
    print(
        "You decide to explore the mansion and find out more about this infamous place...\n"
    )
    time.sleep(5)
    print(
        "You ready yourself against the dangers ahead, and start analysing your surroundings...\n"
    )
    time.sleep(5)

    name = intro()
    game = Game(name)

    # Main game loop
    while True:
        # Show room info
        print(f"==== THE {game.dungeon.get_room_type().upper()} ====")
        game.sleep()
        print(game.dungeon.get_room_intro_message())
        game.sleep()
        input('Press enter to continue: ')
        print()

        # Check for monster in room, if so, fight it
        # This does not require any player interaction for now.
        # It runs automatically and the result of the fight will be displayed
        # in the console immediately.
        monster = game.dungeon.get_monster()
        if monster is not None:
            print(f"There is a {monster.get_type()} here...")
            game.sleep()
            print("It's name is", monster.get_name())
            game.sleep()
            game.rooms_cleared += 1
        win = game.player.fight_monster(monster)
        if not win:  # win may be True, False or None
            game.sleep()
            print("You died...")
            break
        if win is not None:
            game.sleep()
            print("You won the fight!\n")
            heal(game.player)
            print()
            game.player.display_weapon_armor_options()
            print()
        game.dungeon.clear_room()
        num_of_rooms = game.dungeon.get_nums_next_rooms()
        game.sleep()
        print(
            f"There are {num_of_rooms} rooms to enter. \nYou may also go back to the previous room by entering 'back'."
        )
        game.sleep()
        print(game.dungeon.get_next_rooms_message())

        # Get player choice
        choose_room = input("Which room does your heart desire: ")

        while not (
                choose_room.isdigit() and 0 < int(choose_room) <= num_of_rooms
                or choose_room == "back" and game.dungeon.has_previous_room):
            choose_room = input("Invalid.\nEnter a room to enter: ")

        # Enter room
        if choose_room == "back":
            game.dungeon.enter_previous_room()
            print("You have entered the previous room...")
            game.sleep()
            continue
        choose_room = int(choose_room)
        game.dungeon.enter_room(choose_room)

        # Boss battle
        if game.rooms_cleared >= TOTAL_ROOMS:
            boss_fight(game.player)
            break


if __name__ == "__main__":
    main()
