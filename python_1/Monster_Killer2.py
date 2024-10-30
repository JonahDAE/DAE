import random
# Below is for the monsters and the stats. Some or most of the monsters will go unused... But otherwise I will continue this some other time..
CLv = 1
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
artic_ice = 300

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
hellhound = ['hellhound',75,20]
manticore = ['manticore',100,35]
wendigo = ['wendigo',125,40]
#Lv4
reaper = ['reaper',200,50]
mindflayer = ['mindflayer',200,50]
dragon = ['dragon',250,60,]
#Lv5
medusa = ['medusa',300,70]
minotaur = ['minotaur',300,80]
aincient_dragon = ['aincient_dragon',350,99]

Lv1 = [ratbird,goblin,imp,random.randint(1,5)]
Lv2 = [drow,troll,giant,random.randint(6,15)]
Lv3 = [hellhound,manticore,wendigo,random.randint(16,30)]
Lv4 = [reaper,mindflayer,dragon,random.randint(31,50)]
Lv5 = [medusa,minotaur,aincient_dragon,random.randint(51,100)]

levels = [Lv1,Lv2,Lv3,Lv4,Lv5]

weapon = twig
armor = leather
#Here is the definition of the fighting sequence
def fight():
    monster = random.choice(levels)
    if monster == Lv1:
        monster = random.choice(Lv1)
        earnable_gold = Lv1[3]
    elif monster == Lv2:
        monster = random.choice(Lv2)
        earnable_gold = Lv2[3]
    elif monster == Lv3:
        monster = random.choice(Lv3)
        earnable_gold = Lv3[3]
    elif monster == Lv4:
        monster = random.choice(Lv4)
        earnable_gold = Lv4[3]
    elif monster == Lv5:
        monster = random.choice(Lv5)
        earnable_gold = Lv5[3]
    
    monster_def = monster[1]
    monster_str = monster[2]
    
    print('A ' + monster[0] + ' appears!')
    while monster_def != 0:
        print('You draw your weapon and swing...')
        monster_def = monster_def - weapon
        if monster_def < 0:
            monster_def = 0
            killed_monsters = killed_monsters + 1
            print('Congrats! You defeated the ' + monster[0] + ' and gained ' + str(earnable_gold) + ' gold!')
            decision = input('')
            if decision == 'fight':
                fight ()
        if monster_def > 0:
            print('The ' + monster[0] + ' flinches, but attacks back!')
            armor = armor - monster_str
            if armor <= 0:
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
    def play_game():
        print('')
        print('Hello, ' + playername + '!')
        print('You can type \"fight\" to start fighting monsters!')
        print('You can also type \"shop\" to go to the shop and buy items!')
        decision = input('')
        if decision == 'fight':
            fight ()
        else: play_game()
    play_game()