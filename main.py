import room
import introduction
import player
import time
from boss import boss_fight
import food
import monster
import armour
import weapon
import text

TOTAL_ROOMS = 5


class Game:

    def __init__(self, name):
        self.rooms_cleared = 0
        self.dungeon = room.Dungeon()
        self.player = player.Player(name)

    def get_current_room(self) -> str:
        return self.dungeon.get_room_type().upper()

    def get_current_room_message(self) -> str:
        return self.dungeon.get_room_intro_message()

    def get_current_room_monster(self) -> monster.Monster:
        return self.dungeon.get_monster()

    def take_item(self, item: weapon.Weapon | armour.Armour | food.Food) -> None:
        if isinstance(item, weapon.Weapon):
            self.player.weapon = item
        elif isinstance(item, armour.Armour):
            self.player.armor = item
        elif isinstance(item, food.Food):
            self.player.add_health(item.health)
        else:
            raise TypeError(f"{item}: Unrecgonized item type")

    def clear_room(self) -> bool | None:
        """Have the player fight the monster in the current room, if there is one.
        Return the outcome of battle.
        """
        monster = self.get_current_room_monster()
        outcome = self.player.fight_monster(monster)
        if monster:
            self.rooms_cleared += 1
        return outcome


def show_room_info(name: str, message: str) -> None:
    """Display the room information."""
    print(f"==== THE {name} ====")
    pause()
    print(message)
    pause()
    input('Press enter to continue: ')
    print()

def show_monster_info(name: str, type: str) -> None:
    """Display the monster information."""
    print(f"There is a {type} here...")
    pause()
    print("It's name is", name)
    pause()

def pause() -> None:
    time.sleep(1.5)

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
        show_room_info(
            name=game.get_current_room(),
            message=game.get_current_room_message()
        )

        # Check for monster in room, if so, fight it
        # This does not require any player interaction for now.
        # It runs automatically and the result of the fight will be displayed
        # in the console immediately.
        monster = game.get_current_room_monster()
        if monster:
            show_monster_info(
                name=monster.get_name(),
                type=monster.get_type()
            )
        outcome_won = game.clear_room()
        if not outcome_won:  # win may be True, False or None
            pause()
            print("You died...")
            break
        if outcome_won is not None:
            pause()
            print("You won the fight!\n")
            item = food.random_food()
            game.take_item(item)
            print(f"You found a {item.name} and ate it, gaining {item.health} health!")
            print(f"Your health: {game.player.get_health()}")
            time.sleep(3)
            print()
            item = weapon.create_random_weapon()
            print("You found a weapon in the room!")
            time.sleep(1)
            print(f"""
Name: {item.name}
Damage: {item.damage}
Accuracy: {item.accuracy}

{item.description}
""")
            choice = text.prompt_player_choice(
                prompt="Do you want to pick up this weapon?",
                choices={"pick": "Pick up the weapon"},
                validate=False
            )
            if choice == "pick":
                game.take_item(item)
                print("You have picked up the weapon")
            else:
                print("You have ditched the weapon.")

            item = armour.create_random_armour()
            print("\nYou found a piece of armour in the room!")
            time.sleep(1)
            print(f"""
Name: {item.name}
Protection: {item.protection}

{item.description}
""")
            choice = text.prompt_player_choice(
                prompt="Do you want to pick up this armour?",
                choices={"pick": "Pick up the armour"},
                validate=False
            )
            if choice == "pick":
                print("You have picked up the armour")
                game.take_item(item)
            else:
                print("You have ditched the armour.")

        print()
        game.dungeon.clear_room()
        num_of_rooms = game.dungeon.get_nums_next_rooms()
        pause()
        print(
            f"There are {num_of_rooms} rooms to enter. \nYou may also go back to the previous room by entering 'back'."
        )
        pause()
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
            pause()
            continue
        choose_room = int(choose_room)
        game.dungeon.enter_room(choose_room)

        # Boss battle
        if game.rooms_cleared >= TOTAL_ROOMS:
            boss_fight(game.player)
            break


if __name__ == "__main__":
    main()
