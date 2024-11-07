import random
# Below is for the monsters and the stats. Some or most of the monsters will go unused... But otherwise I will continue this some other time..
gold = 0

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
killed_monsters = 0
#Lv1
ratbird = ['ratbird',3,1]
goblin = ['goblin',7,3]
imp = ['imp',4,2]
#Lv2
drow = ['drow',15,5]
troll = ['troll',25,7]
giant = ['giant',35,10]
#Lv3
hellhound = ['hellhound',75,1]
manticore = ['manticore',100,1]
wendigo = ['wendigo',125,1]
#Lv4
reaper = ['reaper',200,1]
mindflayer = ['mindflayer',200,1]
dragon = ['dragon',250,1,]
#Lv5
medusa = ['medusa',300,1]
minotaur = ['minotaur',300,1]
aincient_dragon = ['aincient_dragon',350,1]

#These are the monsters sorted into levels for lists. The random.randint is for gold, they are unused in some of the code because of a problem.
Lv1 = [ratbird,goblin,imp]
Lv2 = [drow,troll,giant]
Lv3 = [hellhound,manticore,wendigo,random.randint(16,30)]
Lv4 = [reaper,mindflayer,dragon,random.randint(31,50)]
Lv5 = [medusa,minotaur,aincient_dragon,random.randint(51,100)]

#The used levels
levels = [Lv1,Lv2]

weapon = wooden
armor = leather
#Here is the definition of the fighting sequence
#This is where a random monster is being chosen at random
def fight():
    armor = 100*random.randint(10,100)
    killed_monsters = 0
    monster = random.choice(levels)
    if monster == Lv1:
        monster = random.choice(Lv1)
    elif monster == Lv2:
        monster = random.choice(Lv2)
    #This is the dialouge and reactions. The dialouge is shown through the print command. The reactions depend on the stats of the characters and weapons.
    monster_def = monster[1]
    monster_str = monster[2]
    print('A ' + monster[0] + ' appears!')
    while monster_def != 0:
        print('You draw your weapon and swing...')
        monster_def = monster_def - weapon
        if monster_def <= 0:
            #You would win your fight against the monster here.
            monster_def = 0
            killed_monsters = killed_monsters + 1
            print('Congrats! You defeated the ' + monster[0] + '!')
            decision = input('')
            if decision == 'fight':
                fight ()
        if monster_def > 0:
            print('The ' + monster[0] + ' flinches, but attacks back!')
            armor = armor - monster_str
            if armor <= 0:
                #Here you would lose.
                print('You have died. GAME OVER')
                monster_def = 0
                gold = gold - (10*killed_monsters)
                if gold < 0:
                    gold = 0

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
    #This command would put a fight between a monster in action.