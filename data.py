"""data.py

Functions for managing game data.

All game data is assumed to be saved in a single folder
"""

import json
import os

DIR_ROOT = "gamedata"


def load(filename: str):
    """Loads a JSON file and returns the contents as a dictionary."""
    path = os.path.join(DIR_ROOT, filename)
    with open(path, "r") as f:
        data = json.load(f)
    return data
