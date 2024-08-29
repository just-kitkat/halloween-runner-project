"""game.py

Module for the main Game class.
"""
import combat
import item
import room


class Game:
    """Encapsulates data for the game."""
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
