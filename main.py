import room 
import introduction
import player
from boss import boss_fight

# from shop import display_shop
# When the game first starts...
# Introduction paragraph
# intro.start_the_game()
# Blackout, spawn in dungeon, game loop begins

# Create player object
player = player.Player()
# introduction.display_startingmsg()
dungeon = room.Dungeon()
rooms_cleared = 0

# Main game loop 
while True:
    # Enter a room
    print(f"Welcome to the {dungeon.get_room_type()}")
    print(dungeon.get_room_intro_message())
    input('Press Enter to continue :')

    # Display monster and start fighting simulation
    # This does not require any player interaction for now.
    # It runs automatically and the result of the fight will be displayed in the console immediately.
    monster = dungeon.get_monster()
    if monster is not None:
        print(f"There is a {monster.get_type()} here...")
        print("It's name is", monster.get_name())
        rooms_cleared += 1
    win = player.fight_monster(monster)
    if win == False: # win may be True, False or None
        print("You died...")
        break
    if win is not None:
        print("You won the fight!")
    dungeon.clear_room()
    num_of_rooms = dungeon.get_nums_next_rooms()
    print(f"There are {num_of_rooms} rooms to enter. \nYou may also go back to the previous room by entering 'back'.")
    print(dungeon.get_next_rooms_message())

    choose_room = input("Which room does your heart desire?:")

    while not (choose_room.isdigit() and 0 < int(choose_room) <= num_of_rooms or choose_room == "back" and dungeon.has_previous_room):
        choose_room = input("Invalid.\nEnter a room to enter: ")
    if choose_room == "back":
        dungeon.enter_previous_room()
        print("You have entered the previous room...")
        continue
    choose_room = int(choose_room)
    dungeon.enter_room(choose_room)

    if rooms_cleared >= 10:
        boss_fight(player)
        break
    

