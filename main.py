import room 
import introduction as intro
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

# When the game first starts...
# Introduction paragraph
intro.start_the_game()
# Blackout, spawn in dungeon, game loop begins
display_blackout_message()

# Create player object
player = create_player()
# Main game loop 
while True:
# create monster, items in the room, create new doors that link to other rooms
    dungeon = room.Dungeon()
    monster = dungeon.get_monster() #call a monster
    fight = player.fight_monster(monster) #player 
    if fight:
        player.collect_items()
    else:
        player.fail_message()
        break
    player.break_action()
    dungeon.clear_room()
    num_of_rooms = dungeon.get_nums_next_room()
    choose_room = int(input("Which room does your heart desire?:"))
    while (choose_room < num_of_rooms) or (choose_room > num_of_rooms):
        choose_room = int(input("Wrong answer. \nWhich room does your heart desire?:"))
    dungeon.enter_room(choose_room)