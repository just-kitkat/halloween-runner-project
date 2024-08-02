import random

class Room:
    def __init__(self, previous_room):
        self.next_rooms = []
        self.previous_room = previous_room
        self.cleared = False
        self.monster = None # Monster object


class Dungeon:
    def __init__(self):
        self.current_room = Room(None)

    def generate_new_rooms(self):
        num_new_rooms = random.randint(2,6)
        self.next_rooms = [Room(self.current_room) for _ in range(num_new_rooms)]
        return self.next_rooms

    def enter_previous_room(self):
        self.current_room = self.current_room.previous_room