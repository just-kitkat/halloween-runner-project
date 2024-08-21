import room 
import introduction
import player as p
import time
"""
Player class:
- name
- health
- inventory
- hunger

Room class:
linked list format, linking rooms together
doors attribute will be a list of Room objects
- linked rooms
- monsters
- items inside (weapons and foods)
- special events
parent class to room types
e.g.
- k    itchen
- main hall
- bathroom
- cellar
- dungeon
- armoury
"""
class Game:
    def __init__(self):
        self.loop = True

    def sleep(self):
        return time.sleep(1)

    def introduction(self):
        # Introduction paragraph
        start = introduction.display_startingmsg()
        return start

    def game_loop(self,name):
        # Create player and room object
        player = p.Player(name)
        dungeon = room.Dungeon()
        # Main game loop 
        while True:
            # Enter a room
            print(f"Welcome to the {dungeon.get_room_type()}")
            self.sleep()
            print(dungeon.get_room_intro_message())
            self.sleep()
            # Display monster and start fighting simulation
            # This does not require any player interaction for now.
            # It runs automatically and the result of the fight will be displayed in the console immediately.
            monster = dungeon.get_monster()
            if monster is not None:
                print(f"There is a {monster.get_type()} here...")
                self.sleep()
                print("It's name is", monster.get_name())
                self.sleep()
            win = player.fight_monster(monster)
            if win == False: # win may be True, False or None
                self.sleep()
                print("You died...")
                break
            if win is not None:
                self.sleep()
                print("You won the fight!")
            dungeon.clear_room()
            num_of_rooms = dungeon.get_nums_next_rooms()
            print(f"There are {num_of_rooms} rooms to enter. \nYou may also go back to the previous room by entering 'back'.")
            print(dungeon.get_next_rooms_message())
        
            choose_room = input("Which room does your heart desire?:")
        
            while not ((choose_room.isdigit()) and (0 < int(choose_room) <= num_of_rooms) or (choose_room == "back" and dungeon.has_previous_room)):
                choose_room = input("Invalid.\nEnter a room to enter: ")
            if choose_room == "back":
                dungeon.enter_previous_room()
                print("You have entered the previous room...")
                continue
            choose_room = int(choose_room)
            dungeon.enter_room(choose_room)

game = Game()
name = game.introduction()
#game.game_loop(name)