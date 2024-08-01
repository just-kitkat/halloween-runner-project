import methods 
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
- kitchen
- main hall
- bathroom
- cellar
- dungeon
- armoury
"""

# When the game first starts...
# Introduction paragraph
display_introduction()

# Blackout, spawn in dungeon, game loop begins
display_blackout_message()

# Create player object
player = create_player()
# Main game loop 
while True:
    # create monster, items in the room, create new doors that link to other rooms
    current_room = Dungeon()
    current_room.getMonster()
    player.fightMonster()
    player.collectItems()
    player.breakAction()
    current_room.displayNewRooms()
    player.chooseRoom()
    "you can use items, however the more actions you take the higher the chance that monsters would come back in"# Include this in the player.breakAction() method
    display_break_message() # allow users to eat and use items

    display_room_options()