
step = 0
print('Hello! Today we are baking a cake! Before we begin, what is your name?')
Name = input('')
print('Nice to meet you, ' + Name + 'I hope you\'re excited to make your first cake, because we are getting started now!')
print('On step one, preheat the oven to 350 degrees')
print('What will you preheat the oven to?')
preheat = input('')
if preheat == '350':
    step = step + 1
    print('Great! Now we\'ll work on adding ingredients!')
    print('Now we just add in eggs, flour, sugar, and... I\'m forgetting something...')
    ingredient = input('')
    if ingredient == 'milk':
        step = step + 1
        print('I remember what we need now! Lots of milk!')
        print('Now we are ready to put our cake in the oven! Just bake it for 45 minutes...')
        print('How many minutes will the cake be baked for?')
        time = input('')
        if time == '45':
            step = step + 1
            print('Finally! We\'re finished making our cake! Thanks for helping, ' + Name + '!')
            print('GAME END!')
            print('Steps done: ',step)
        else:
            print('The oven was left on too long and lit the building on fire. And you died.')
            print('Steps done: ',step)
            print('Try again!')
    else:
        print('You mixed up the ingredients and we all died.')
        print('steps done: ',step)
        print('Try again!')
else:
    print('You preheated the oven wrong and we all died.')
    print('steps done: ',step)
    print('Try again!')