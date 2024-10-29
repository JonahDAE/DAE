import random
# Below is for the monsters and the stats. Some or most of the monsters will go unused... But otherwise I will continue this some other time..
Gold = 0

#Weapons
twig = 1
wooden = 5
beaten = 10
avg_sword = 25
stainless_steel = 50
holy = 75
heatsaber = 101

#Armor
none = 5
leather = 25
chainmail = 50
knight = 75
obsidian = 100
holy = 150
articice = 300

#Monsters
#Lv1
ratbird = ['ratbird',3,1]
goblin = ['goblin',7,3]
imp = ['imp',4,2]
#Lv2
drow = ['drow',15,5]
troll = ['troll',25,7]
giant = ['giant',35,10]
#Lv3
Hellhound = 75
manticore = 100
wendigo = 125
#Lv4
Reaper = 200
mindflayer = 200
dragon = 250
#Lv5
medusa = 300
minotaur = 300
aincient_Dragon = 350

Lv1 = [ratbird,goblin,imp]
Lv2 = [drow,troll,giant]

randomlevel = [Lv1,Lv2]

weapon = wooden
armor = leather
#Here is the definition of the fighting sequence
def fight():
    armor = 25
    monster = random.choice(randomlevel)
    if monster == Lv1:
        monster = random.choice(Lv1)
    elif monster == Lv2:
        monster = random.choice(Lv2)
    
    monster_def = monster[1]
    monster_str = monster[2]
    
    print('A ' + monster[0] + ' appears!')
    while monster_def != 0:
        print('You draw your weapon and swing...')
        monster_def = monster_def - weapon
        if monster_def < 0:
            monster_def = 0
            print('Congrats! You defeated the ' + monster[0] + '! Type \"fight\" to fight another.')
            decision = input('')
            if decision == 'fight':
                fight ()
        if monster_def > 0:
            print('The ' + monster[0] + ' flinches, but attacks back!')
            armor = armor - monster_str
            if armor <= 0:
                print('You have died. GAME OVER')
                monster_def = 0



#This is where the game begins
print('Hello! Welcome to Monster Killer, the game about killing monsters!')
print('Enter your name here:')
playername = input('')
gameactive = 'yes'
if gameactive == 'yes':
    print('')
    print('Hello, ' + playername + '!')
    print('You can type \"fight\" to start fighting monsters!')
    decision = input('')
    if decision == 'fight':
        fight ()