import room 
# import introduction as intro
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
from shop import display_shop
# When the game first starts...
# Introduction paragraph
# intro.start_the_game()
# Blackout, spawn in dungeon, game loop begins

# Create player object
player = player.Player()
# Main game loop 
while True:
# Intro
    # create monster, items in the room, create new doors that link to other rooms
    initialise_room()

    fight_monster()

    collect_items()

    "you can use items, however the more actions you take the higher the chance that monsters would come back in"
    display_break_message() # allow users to eat and use items

    display_shop()

    display_room_options()
# create monster, items in the room, create new doors that link to other rooms
    dungeon = room.Dungeon()
    monster = dungeon.get_monster() #call a monster
    fight = player.fight_monster(monster) #player 
    # if fight:
    #     player.collect_items()
    # else:
    #     player.fail_message()
    #     break
    # player.break_action()
    print(dungeon.clear_room())
    num_of_rooms = dungeon.get_nums_next_rooms()
    choose_room = int(input("Which room does your heart desire?:"))
    while (choose_room < 1) or (choose_room > num_of_rooms):
        choose_room = int(input("Wrong answer. \nWhich room does your heart desire?:"))
    dungeon.enter_room(choose_room)

