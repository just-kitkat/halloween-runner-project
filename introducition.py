def error_msg():
    print('I\'m not sure I understand.')

def display_startingmsg():
    print("Welcome to Eek MUD! Are you ready for an adventure? Let's go!")
    ye = True
    while ye:
        char = input("Press C to start and Press E to exit. ")
        char = char.strip().upper()
        if char not in ['C', 'E']:
            error_msg()
        else:
            ye = False
    if char == 'C':
        name = player_name()
        print(f'Welcome {name}! Enjoy the game!')
        game_start(name)
    elif char == 'E':
        print("Thanks for playing!")
        return False

def player_name():
    yes = True
    while yes:
        name = input('What would you like your player name to be? ')
        if name in ['', ' ']:
            error_msg()
        else:
            yes = False
    name = name.strip()
    name = name.title()
    return name

def game_start(name):
        
        display_intromsg(name)
        the_three_actions(name)

def display_intromsg(name):
    print("Tonight is October 31st, the night known as \nHalloween. \nAfter escaping your friend's raucous Halloween party, you find yourself aimlessly wandering deeper into the shadowy woods. The darkness thickens, enveloping you in an eerie silence. \n ... \nHours pass in your solitary journey until you stumble upon a colossal, foreboding castle. It looks disturbingly familiar, and with a chill, you realize \n ... \nit is the infamous Nanyang Mansion. Whispers of children vanishing within its walls have haunted you, stories you always dismissed and never believed in. \n \nTonight, you will uncover the truth. Tonight, \nyou will prove them wrong.")
    print('')
    print('Are you up for the challenge?' +
                    '\n1)yes \n2)yes \n3)yes')
    input(f'{name}\'s input: ')
    print('You walk up the long flight of stairs that lead up to a pair of large, mahogany doors. \nYou push the doors open slowly, and a large creak echoes through the expansive space. A dark, forbidding hall greets you. \nIt’s musty, and cobwebs lie all around. \nSmoke slowly penetrates through the floor and dust fills the atmosphere of the quiet, sordid expanse. At the corner of your eye, you see a red object lurking in the dark, at the same time, you feel something swift past behind you.')

def the_three_actions(name):
    for i in range(3):
        ye = True
        while ye:
            print('What do you do next? \n1) Move forward \n2) Turn around and look \n3) Don\'t do anything')
            option1 = input(f'{name}\'s input: ') 
            if option1 not in ['1', '1)', '2', '2)', '3', '3)']:
                error_msg()
            else:
                ye = False
        if option1 in ['1', '1)']:
            action_1()
        elif option1 in ['2', '2)']:
            action_2()
        elif option1 in['3', '3)']:
            action_3()

    blackout_msg()


def action_3():
    print("You hear the faint echo of distant whispers, the creak of ancient floorboards, and the occasional soft thud as if something unseen is moving nearby. Despite the unsettling noises, nothing happens, leaving you in a tense, nerve-wracking stillness that makes every shadow seem alive.")

def action_1():
    print('As you move forward through the dark castle, a shadow suddenly darts past you, too quick to see clearly. Heart pounding, you freeze, waiting for something to happen. But nothing does. The silence presses in, and the tension mounts with each step, knowing something is lurking just out of sight.')

def action_2():
    print('Turning around quickly, you peer into the darkness, but there’s nothing there. Just an empty, silent corridor. The hairs on the back of your neck stand up as the oppressive silence presses in, leaving you with the unsettling feeling that you’re not alone.')

def blackout_msg():
    print('As you turn around, something hard strikes the back of your head. Pain explodes through your skull, and your vision blurs. The last thing you see before everything goes black is the cold, dark corridor closing in around you. \n...\n')
