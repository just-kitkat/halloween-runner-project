import random

import monster
from room_messages import msg

counter = {}


class Room:

    def __init__(self, previous_room, room_type=None):
        self.next_rooms: list["Room"] = []

        if room_type is None:
            room_type = random.choice(list(msg.keys()))
        self.type = room_type

        if self.type in counter:
            room_type += " " + str(counter[self.type] + 1)
            counter[self.type] += 1
        else:
            counter[self.type] = 1
        self.display_type = room_type

        self.previous_room = previous_room
        self.cleared = False
        #updated line below
        self.monster = monster.create_random_monster()
        if previous_room is None:
            self.monster = None

    def get_type_display(self):
        return self.display_type

    def get_next_rooms(self) -> tuple["Room", ...]:
        """Return a tuple to avoid the original list getting modified."""
        return tuple(self.next_rooms)


class Dungeon:

    def __init__(self):
        # When the game first starts, a room is created.
        self.current_room = Room(None)
        self.number_of_rooms_visited = 0

    def get_monster(self) -> monster.Monster:
        return self.current_room.monster

    def is_room_cleared(self):
        return self.current_room.cleared

    def get_room_type_display(self):
        return self.current_room.get_type_display()

    def get_room_intro_message(self):
        room_type = self.current_room.type
        if room_type is not None:
            return random.choice(msg[room_type])
        raise ValueError("self.current_room.type has an invalid valie of",
                         room_type)

    def get_next_rooms_message(self) -> str:
        next_rooms = self.current_room.get_next_rooms()
        if not next_rooms:
            return "Clear the room first!"

        msg = f"There are {len(next_rooms)} rooms.\n"
        for i, room in enumerate(next_rooms, start=1):
            msg += f"{i}. {room.get_type_display()}\n"
        return msg

    def __generate_next_rooms(self):
        num_new_rooms = random.randint(2, 6)
        self.current_room.next_rooms = [
            Room(self.current_room) for _ in range(num_new_rooms)
        ]
        return self.get_next_rooms_message()

    def clear_room(self):
        self.monster = None
        if self.current_room.cleared:
            return self.get_next_rooms_message()
        self.current_room.cleared = True
        return self.__generate_next_rooms()

    def enter_room(self, idx):  # idx should be 1-indexed
        self.current_room = self.current_room.next_rooms[idx - 1]

    def has_previous_room(self) -> bool:
        return self.current_room.previous_room is not None

    def enter_previous_room(self):
        if self.current_room.previous_room is None:
            return False
        cleared = self.is_room_cleared()
        if cleared:
            self.current_room = self.current_room.previous_room
        return cleared

    def get_room_type(self):
        return self.current_room.type


# The below code is used for testing, please do not remove
if __name__ == "__main__":
    dungeon = Dungeon()
    dungeon.clear_room()
    # print(dungeon.enter_previous_room())
    print(dungeon.get_room_intro_message())
    print(dungeon.get_next_rooms_message())
    dungeon.enter_room(1)
    # print(dungeon.display)
    dungeon.clear_room()
    print(dungeon.get_room_intro_message())
    print(dungeon.get_next_rooms_message())
    dungeon.enter_previous_room()
    print(dungeon.get_room_type())
    print(dungeon.get_room_intro_message())
    print(dungeon.get_next_rooms_message())
