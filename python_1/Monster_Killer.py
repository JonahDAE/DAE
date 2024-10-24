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
ratbird = 3
goblin = 7
imp = 4
#Lv2
drow = 15
troll = 25
giant = 35
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

monsterlvl_dict = {lv1 = [ratbird, goblin, imp] lv2 = [drow, troll, giant] lv3 = [Hellhound, manticore, wendigo]}

weapon = twig
armor = leather

print('Hello! Welcome to Monster Killer, the game about killing monsters!')
print('Enter your name here:')
playername = input('')
gameactive = 'yes'
if gameactive == 'yes':
    print('')
    print('Hello, ' + playername + '!')
    print('You can type \"fight\" to start fighting monsters!')
    print('You can also type \"shop\" to buy gear with gold.')
    decision = input('')