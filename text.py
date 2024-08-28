"""text.py

Functions for handling text input and display.
"""

def prompt_player_choice(
    prompt: str,
    choices: dict[str, str],
    question: str = "Your choice: ",
    validate: bool = True
):
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