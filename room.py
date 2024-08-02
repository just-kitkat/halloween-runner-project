import random

class Room:
    def __init__(self, previous_room):
        self.next_rooms = []
        self.previous_room = previous_room
        self.cleared = False
        self.monster = None # Monster object


class Dungeon:
    def __init__(self):
        # When the game first starts, a room is created.
        self.current_room = Room(None)
        self.number_of_rooms_visited = 0

    def get_monster(self):
        return self.current_room.monster

    def is_room_cleared(self):
        return self.current_room.cleared

    def generate_new_rooms(self):
        num_new_rooms = random.randint(2,6)
        self.next_rooms = [Room(self.current_room) for _ in range(num_new_rooms)]
        return self.next_rooms

    def clear_room(self):
        self.current_room.cleared = True

    def enter_previous_room(self):
        cleared = self.is_room_cleared()
        if cleared:
            self.current_room = self.current_room.previous_room
        return cleared

if __name__ == "__main__":
    # Used for testing
    dungeon = Dungeon()
    print(dungeon.generate_new_rooms())
    dungeon.clear_room()
    print(dungeon.enter_previous_room())