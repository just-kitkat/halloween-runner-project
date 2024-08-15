import room 
import introduction
import player
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
# from shop import display_shop
# When the game first starts...
# Introduction paragraph
# intro.start_the_game()
# Blackout, spawn in dungeon, game loop begins

# Create player object
player = player.Player()
# introduction.display_startingmsg()
dungeon = room.Dungeon()

# Main game loop 
while True:
    # Enter a room
    print(dungeon.get_room_intro_message())

    monster = dungeon.get_monster()
    if monster is not None:
        print(f"There is a {monster.mob} here...")
        print("It's name is", monster.name)
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
    print(dungeon.has_previous_room)
    while not (choose_room.isdigit() or choose_room == "back" and dungeon.has_previous_room):
        choose_room = input("Invalid.\nEnter a room to enter: ")
    if choose_room == "back":
        dungeon.enter_previous_room()
        print("You have entered the previous room...")
        continue
    choose_room = int(choose_room)
    dungeon.enter_room(choose_room)

