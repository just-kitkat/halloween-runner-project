import random

def monster_name_generator():
    first_name = ['Grim', 'Mortis', 'Thorne', 'Vex', 'Hex', 'Nyx', 'Dread', 'Wraith', 'Shade', 'Gloom', 'Ethan', 'Seah', 'Joshua', 'Wong', 'Cho']
    last_name = ['Nightshade', 'Bloodbane', 'Frostmourne', 'Grimspike', 'Darkwhisper', 'Deathclaw', 'Skullrend', 'Shadowfang', 'Wraithborn', 'Ironshade', 'Wang', 'Eket', 'Zijia', 'Zin']
    lenf = len(first_name)
    lenl = len(last_name)
    num1 = random.randint(0, lenf-1)
    num2 = random.randint(0, lenl-1)
    monster_name = f'{first_name[num1]} {last_name[num2]}'
    return monster_name