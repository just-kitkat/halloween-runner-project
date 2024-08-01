def display_startingmsg():
    print("Welcome to Eek MUD! Are you ready for an adventure? Let's go!")

def game_start():
    char = input("Press C to start and Press E to exit.")
    if char.upper() == 'C':
        display_intromsg()
    elif char.upper() == 'E':
        print("Thanks for playing!")
        return False

def display_intromsg():
    print("It is Halloween night. After escaping from your friend’s loud Halloween party, you find yourself wandering in the woods. As the night grows darker, you get deeper into the woods. After hours and hours of your solo-expedition, you find a big spooky castle. It looked eerily familiar, and you realise it is the infamous Nanyang Mansion. You’ve heard of stories of children disappearing after going into the mansion, but you never believed in those tales." + '\n' + 'Tonight is the night to prove to them you are right.' + '\n')
    print('')
    print('Are you up for the challenge?')

# 1) LET’S DO IT.
# 2) Sure?
# [this one just to hype up ah it doesn’t do anything]

# You walk up the long flight of stairs that lead up to a pair of large, mahogany doors. You push the doors open slowly, and a large creak echoes through the expansive space. A dark, forbidding hall greets you. It’s musty, and cobwebs lie all around. Smoke slowly penetrates through the floor and dust fills the atmosphere of the quiet, sordid expanse. At the corner of your eye, you see a red object lurking in the dark, at the same time, you feel something swift past behind you.

# What do you do next?
# 1) Move forward to find out the red object is
# 2) Turn around and look
# Eek’s input: 1

# You move forward but before you can reach the object, something hits you from behind and you black out.
# ")