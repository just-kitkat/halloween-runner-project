import room 
import introducition as intro
import player
import input_checker as check
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
start = intro.display_startingmsg()
# Blackout, spawn in dungeon, game loop begins
player = player.Player()# Create player object
# Main game loop 
dungeon = room.Dungeon() #initialize dungeon
while start:
# create monster, items in the room, create new doors that link to other rooms
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

