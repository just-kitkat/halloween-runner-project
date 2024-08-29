"""script.py

Functions for:
- handling text input and display
- handling scripted interactions (e.g. combat)

"""
import time

import combat
import data
import introduction
import item
import runner


## Helper functions

def short_pause() -> None:
    time.sleep(1.5)

def medium_pause() -> None:
    time.sleep(3)

def long_pause() -> None:
    long_pause()

def a_or_an(word: str) -> str:
    """Returns the correct article for a given word."""
    return f"an {word}" if word[0] in "aeiou" else f"a {word}"

def prompt_player_choice(prompt: str,
                         choices: dict[str, str],
                         question: str = "Your choice: ",
                         validate: bool = True):
    """Prompts the player to make a choice.
    
    Arguments:
    - prompt: str
      The prompt to display to the player.
    - choices: {str: str}
      A dictionary of choices, with choice labels as keys, and descriptions
      as values
    - validate: bool [default True]
      Whether to validate the player's choice. If True, the player will be
      prompted to enter a choice until a valid choice is made.
    """
    choice = None
    while choice is None:
        print(prompt)
        for option, description in choices.items():
            print(f"{option}: {description}")
        choice = input(question)
        if validate and choice not in choices:
            print("Invalid choice. Please try again.")
            choice = None
    return choice


## Display functions

def show_room_info(name: str, message: str) -> None:
    """Display the room information."""
    print(f"==== THE {name} ====")
    short_pause()
    print(message)
    short_pause()
    input('Press enter to continue: ')
    print()


def show_monster_info(name: str, type: str) -> None:
    """Display the monster information."""
    print(f"There is a {type} here...")
    short_pause()
    print("It's name is", name)
    short_pause()


def show_item_info(item_: item.Item) -> None:
    if isinstance(item_, item.Weapon):
        itemtype = "weapon"
    elif isinstance(item_, item.Armor):
        itemtype = "armor"
    elif isinstance(item_, item.Food):
        itemtype = "food"
    else:
        itemtype = "item"
    print(f"You found {a_or_an(itemtype)} in the room!")
    print(item_.info())
    short_pause()


def show_strike_info(result: combat.StrikeResult) -> None:
    """Display information about the outcome of the battle strike"""
    if not result.hit:
        print(f"{result.attacker_name}'s attack missed!")
        return
    print(
        f"{result.attacker_name} attacked {result.defender_name} with \"{result.attacker_weapon}\", dealing {result.damage} damage"
    )
    if result.reduction:
        print(
            f"{result.defender_name}'s armour protected them from {result.reduction} damage!"
        )


def show_item_result(item_: item.Item, choice: str | None = None):
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
        medium_pause()


# Scripted functions

def before_intro():
    # Continuation of storyline from blackout
    print("You wake up and find youself in a mysterious place...\n")
    long_pause()
    print(
        "You decide to explore the mansion and find out more about this infamous place...\n"
    )
    long_pause()
    print(
        "You ready yourself against the dangers ahead, and start analysing your surroundings...\n"
    )
    long_pause()


def intro():
    start = introduction.display_startingmsg()
    return start


def no_monsters():
    print("There are no monsters in this room!")


def game_over():
    short_pause()
    print("You died...")


def battle_won(game):
    short_pause()
    print("You won the fight!\n")
    give_reward(game, "food")
    give_reward(game, "weapon", autopickup=False)
    give_reward(game, "armour", autopickup=False)


def run_battle_loop(player: combat.Player, enemy: combat.Combatant) -> None:
    """Run battle loop until either player or enemy is dead."""
    room_battle = combat.Battle(player, enemy)
    while not room_battle.is_ended():
        for result in room_battle.exchange():
            show_strike_info(result)
        input("Press enter to continue: ")


def choose_next_room(game: runner.Game) -> str:
    """Menu where player chooses next room.
    Returns player choice.
    """
    rooms = game.dungeon.get_next_rooms()
    prompt = f"There are {len(rooms)} rooms to enter."
    choices = {
        str(i): room.get_type_display()
        for i, room in enumerate(rooms, start=1)
    }
    if game.dungeon.has_previous_room:
        choices['back'] = "Go back to the previous room"
    short_pause()
    # Get player choice
    choice = prompt_player_choice(
        prompt=prompt,
        choices=choices,
        question="Which room does your heart desire: ",
        validate=True)
    return choice


def boss_fight(player: combat.Player):
    """Lead-up to the boss fight, plus boss fight"""
    boss_entry = data.load("boss.json")
    for msg in boss_entry["enter_room"]:
        print(msg)
        medium_pause()

    boss = combat.create_boss()
    run_battle_loop(player, boss)

    if player.is_dead():
        msgs = boss_entry["player_win"]
    elif boss.is_dead():
        msgs = boss_entry["player_lose"]
    for msg in msgs:
        print(msg)
        long_pause()


def give_reward(game: runner.Game, reward: str, autopickup: bool = True):
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
        choice = prompt_player_choice(
            prompt=f"Do you want to pick up this {reward}?",
            choices={"pick": f"Pick up the {reward}"},
            validate=False)
    else:
        choice = None
    # Handle player choice (if any), show result of item
    if choice == "pick":
        game.take_item(item_)
    show_item_result(item_, choice)
