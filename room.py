import random
from monster import create_monster,all_monsters
from room_messages import msg

class Room:
    def __init__(self, previous_room, room_type=None):
        self.next_rooms = []
        self.type = room_type
        if self.type is None:
            self.type = random.choice(list(msg.keys()))
        self.previous_room = previous_room
        self.cleared = False
        #updated line below
        self.monster = None #create_monster(random.choice(all_monsters())) #Monster object
        if previous_room is None:
            self.monster = None

    def get_next_rooms(self):
        if len(self.next_rooms) == 0:
            return "Clear the room first!"

        msg = f"There are {len(self.next_rooms)} rooms.\n"
        count = 1
        for room in self.next_rooms:
            msg += f"{count}. {room.type}\n"
            count += 1
        return msg

    def get_num_next_rooms(self):
        return len(self.next_rooms)
        

class Dungeon:
    def __init__(self):
        # When the game first starts, a room is created.
        self.current_room = Room(None)
        self.number_of_rooms_visited = 0

    def get_monster(self):
        return self.current_room.monster

    def is_room_cleared(self):
        return self.current_room.cleared

    def get_nums_next_rooms(self):
        return self.current_room.get_num_next_rooms()

    def get_room_intro_message(self):
        room_type = self.current_room.type
        if room_type is not None:
            return random.choice(msg[room_type])
        raise ValueError("self.current_room.type has an invalid valie of", room_type)

    def get_next_rooms_message(self):
        return self.current_room.get_next_rooms()

    def __generate_next_rooms(self):
        num_new_rooms = random.randint(2,6)
        self.current_room.next_rooms = [Room(self.current_room) for _ in range(num_new_rooms)]
        return self.get_next_rooms_message()

    def clear_room(self):
        if self.current_room.cleared:
            return self.get_next_rooms_message()
        self.current_room.cleared = True
        return self.__generate_next_rooms()

    def enter_room(self, idx): # idx should be 1-indexed
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