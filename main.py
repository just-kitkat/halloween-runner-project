import room 
import introduction
import player as p
import time
from boss import boss_fight
from food import use

# from shop import display_shop
# When the game first starts...
# Introduction paragraph
# intro.start_the_game()
# Blackout, spawn in dungeon, game loop begins
class Game:
    def __init__(self):
        self.rooms_cleared = 0

    def intro(self):
        start = introduction.display_startingmsg()
        return start

    def sleep(self):
        return time.sleep(1.5)

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
            input('Press Enter to continue :')
            
            # Display monster and start fighting simulation
            # This does not require any player interaction for now.
            # It runs automatically and the result of the fight will be displayed in the console immediately.
            monster = dungeon.get_monster()
            if monster is not None:
                print(f"There is a {monster.get_type()} here...")
                self.sleep()
                print("It's name is", monster.get_name())
                self.sleep()
                self.rooms_cleared += 1
            win = player.fight_monster(monster)
            if win == False: # win may be True, False or None
                self.sleep()
                print("You died...")
                break
            if win is not None:
                self.sleep()
                print("You won the fight!")
                player.display_weapon_armor_options()
            dungeon.clear_room()
            num_of_rooms = dungeon.get_nums_next_rooms()
            self.sleep()
            print(f"There are {num_of_rooms} rooms to enter. \nYou may also go back to the previous room by entering 'back'.")
            self.sleep()
            print(dungeon.get_next_rooms_message())
        
            choose_room = input("Which room does your heart desire?:")
        
            while not (choose_room.isdigit() and 0 < int(choose_room) <= num_of_rooms or choose_room == "back" and dungeon.has_previous_room):
                choose_room = input("Invalid.\nEnter a room to enter: ")
            if choose_room == "back":
                dungeon.enter_previous_room()
                print("You have entered the previous room...")
                self.sleep()
                continue
            choose_room = int(choose_room)
            dungeon.enter_room(choose_room)
        
            if self.rooms_cleared >= 10:
                boss_fight(player)
                break
            



game = Game()
name = game.intro()
game.game_loop(name)