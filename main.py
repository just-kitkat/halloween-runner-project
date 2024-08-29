import room
import introduction
import player
import time
from boss import boss_fight
import battle
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

    def clear_room(self) -> None:
        """Assumes the player won the battle, clear the current room."""
        self.rooms_cleared += 1
        self.dungeon.clear_room()


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

def show_item_info(item: weapon.Weapon | armour.Armour | food.Food) -> None:
    if isinstance(item, weapon.Weapon):
        itemtype = "weapon"
    elif isinstance(item, armour.Armour):
        itemtype = "armour"
    elif isinstance(item, food.Food):
        itemtype = "food"
    a_or_an_item = f"an {itemtype}" if itemtype[0] in "aeiou" else f"a {itemtype}"
    print(f"You found {a_or_an_item} in the room!")
    print(item.info())
    time.sleep(1)

def show_strike_info(result: battle.StrikeResult) -> None:
    """Display information about the outcome of the battle strike"""
    if not result.hit:
        print(f"{result.attacker_name}'s attack missed!")
        return
    print(
        f"{result.attacker_name} attacked {result.defender_name} with \"{result.attacker_weapon}\", dealing {result.damage} damage"
    )
    if result.reduction:
        print(f"{result.defender_name}'s armour protected them from {result.reduction} damage!")

def show_item_result(
        game: Game,
        item: weapon.Weapon | armour.Armour | food.Food,
        choice: str | None = None
):
    if isinstance(item, weapon.Weapon):
        if choice == 'pick':
            print(f"You took the {item.name}")
        else:
            print(f"You ditched the {item.name}")
    elif isinstance(item, armour.Armour):
        if choice == 'pick':
            print(f"You took the {item.name}")
        else:
            print(f"You ditched the {item.name}")
    elif isinstance(item, food.Food):
        print(f"You ate the {item.name}, gaining {item.health} health!")
        print(f"Your health: {game.player.get_health()}")
        time.sleep(3)

def give_reward(game: Game, reward: str, autopickup: bool = True):
    """Macro function to handle player reward after fight."""
    if reward == "food":
        item = food.random_food()
    elif reward == "weapon":
        item = weapon.create_random_weapon()
    elif reward == "armour":
        item = armour.create_random_armour()
    else:
        raise ValueError(f"Invalid reward: {reward}")
    show_item_info(item)
    # Prompt player to pick up item (if required)
    if not autopickup:
        choice = text.prompt_player_choice(
            prompt=f"Do you want to pick up this {reward}?",
            choices={"pick": f"Pick up the {reward}"},
            validate=False
        )
    else:
        choice = None
    # Handle player choice (if any), show result of item
    if choice == "pick":
        game.take_item(item)
    show_item_result(game, item, choice)

def pause() -> None:
    time.sleep(1.5)

def intro():
    start = introduction.display_startingmsg()
    return start

def game_over():
    pause()
    print("You died...")
    exit()

def no_monsters():
    print("There are no monsters in this room!")

def battle_won(game):
    pause()
    print("You won the fight!\n")
    give_reward(game, "food")
    give_reward(game, "weapon", autopickup=False)
    give_reward(game, "armour", autopickup=False)


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
            room_battle = battle.Battle(game.player, monster)
            while not room_battle.is_ended():
                for result in room_battle.exchange():
                    show_strike_info(result)
            if game.player.is_dead():
                game_over()
            elif monster.is_dead():
                battle_won(game)
                game.clear_room()
        else:
            no_monsters()
        rooms = game.dungeon.get_next_rooms()
        prompt = f"There are {len(rooms)} rooms to enter."
        choices = {
            str(i): room.get_type_display()
            for i, room in enumerate(rooms, start=1)
        }
        if game.dungeon.has_previous_room:
            choices['back'] = "Go back to the previous room"
        pause()
        # Get player choice
        choice = text.prompt_player_choice(
            prompt=prompt,
            choices=choices,
            question="Which room does your heart desire: ",
            validate=True
        )
        pause()

        # Enter room
        if choice == "back":
            game.dungeon.enter_previous_room()
            print("You have entered the previous room...")
            pause()
            continue
        game.dungeon.enter_room(int(choice))

        # Boss battle
        if game.rooms_cleared >= TOTAL_ROOMS:
            boss_fight(game.player)
            break


if __name__ == "__main__":
    main()
