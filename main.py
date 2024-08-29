import data
import room
import introduction
import time
import battle
import text
import combat
import item

TOTAL_ROOMS = 5


class Game:

    def __init__(self, name):
        self.rooms_cleared = 0
        self.dungeon = room.Dungeon()
        self.player = combat.create_player(name)

    def get_current_room(self) -> str:
        return self.dungeon.get_room_type().upper()

    def get_current_room_message(self) -> str:
        return self.dungeon.get_room_intro_message()

    def get_current_room_monster(self) -> combat.Monster:
        return self.dungeon.get_monster()

    def take_item(self, item_: item.Item) -> None:
        if isinstance(item_, item.Food):
            self.player.add_health(item_.health)
        else:
            self.player.take_item(item_)

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

def show_item_info(item_: item.Item) -> None:
    if isinstance(item_, item.Weapon):
        itemtype = "weapon"
    elif isinstance(item_, item.Armor):
        itemtype = "armor"
    elif isinstance(item_, item.Food):
        itemtype = "food"
    a_or_an_item = f"an {itemtype}" if itemtype[0] in "aeiou" else f"a {itemtype}"
    print(f"You found {a_or_an_item} in the room!")
    print(item_.info())
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
        item_: item.Item,
        choice: str | None = None
):
    if isinstance(item_, item.Weapon):
        if choice == 'pick':
            print(f"You took the {item_.name}")
        else:
            print(f"You ditched the {item_.name}")
    elif isinstance(item_, item.Armor):
        if choice == 'pick':
            print(f"You took the {item_.name}")
        else:
            print(f"You ditched the {item_.name}")
    elif isinstance(item_, item.Food):
        print(f"You ate the {item_.name}, gaining {item_.health} health!")
        print(f"Your health: {game.player.get_health()}")
        time.sleep(3)

def give_reward(game: Game, reward: str, autopickup: bool = True):
    """Macro function to handle player reward after fight."""
    if reward == "food":
        item_ = item.random_food()
    elif reward == "weapon":
        item_ = item.random_weapon()
    elif reward == "armour":
        item_ = item.random_armor()
    else:
        raise ValueError(f"Invalid reward: {reward}")
    show_item_info(item_)
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
        game.take_item(item_)
    show_item_result(game, item_, choice)

def boss_fight(player):
    boss_entry = data.load("boss.json")
    for msg in boss_entry["enter_room"]:
        print(msg)
        time.sleep(3)

    boss = combat.create_boss()
    final_battle = battle.Battle(player, boss)
    while not final_battle.is_ended():
        for result in final_battle.exchange():
            show_strike_info(result)
        input("Press enter to continue: ")

    if player.is_dead():
        msgs = boss_entry["player_win"]
    elif boss.is_dead():
        msgs = boss_entry["player_lose"]
    for msg in msgs:
        print(msg)
        time.sleep(5)


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
                name=monster.name,
                type=monster.type
            )
            room_battle = battle.Battle(game.player, monster)
            while not room_battle.is_ended():
                for result in room_battle.exchange():
                    show_strike_info(result)
                input("Press enter to continue: ")
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
