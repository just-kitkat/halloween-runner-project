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
from shop import display_shop
# When the game first starts...
# Introduction paragraph
display_introduction()

# hello eket/ will there be a class for player that includes the health of the player and the items it has and stuff stuff

# Blackout, spawn in dungeon, game loop begins
display_blackout_message()

# Create player object
player = create_player()
# Main game loop 
while True:
    # create monster, items in the room, create new doors that link to other rooms
    initialise_room()

    fight_monster()

    collect_items()

    "you can use items, however the more actions you take the higher the chance that monsters would come back in"
    display_break_message() # allow users to eat and use items

    display_shop()

    display_room_options()