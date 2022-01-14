##!/usr/bin/env python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import assets
import random
import time
import platform
import os


# start the player in the Default location
currentRoom = assets.starterRoom
previousRoom = ''

# an inventory, which is initially empty
inventory = []

#Used to clear screen
def clr_scr():
    # Check if the platform is Windows or linux
    # If Platform is Windows then run command os.system(‘cls’) else os.system(‘clear’)
    if (platform.system().lower() == "windows"):
        cmdtorun = 'cls'
    else:
        cmdtorun = 'clear'

    os.system(cmdtorun)
#Lists commands available from current room.
def commandlist():
    print('Commands available for this room:')
    if 'go' in assets.rooms[currentRoom]:
        print('go')
    if 'get' in assets.rooms[currentRoom]:
        print('get')
    if 'open' in assets.rooms[currentRoom]:
        print('open')


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    ''')


#Lists directions available from current room.
def directions():
    print('You can go:')
    if 'north' in assets.rooms[currentRoom]:
        print('North to ' + assets.rooms[currentRoom]['north'])
    if 'south' in assets.rooms[currentRoom]:
        print('South to ' + assets.rooms[currentRoom]['south'])
    if 'east' in assets.rooms[currentRoom]:
        print('East to ' + assets.rooms[currentRoom]['east'])
    if 'west' in assets.rooms[currentRoom]:
        print('West to ' + assets.rooms[currentRoom]['west'])


#Establishes current status
def showStatus():
    """determine the current status of the player"""
    # print the player's current status
    print('---------------------------')
    print(f'You are in the {currentRoom}')
    print(assets.rooms[currentRoom]['desc'])
    print('---------------------------')
    commandlist()
    # print an item if there is one
    if 'item' in assets.rooms[currentRoom]:
        if assets.rooms[currentRoom]['item'] != '':
            print('You see ' + assets.rooms[currentRoom]['item'] + ' in the room.')
    if 'container' in assets.rooms[currentRoom]:
        print(assets.rooms[currentRoom]['containerloc'])
    print('---------------------------')
    directions()
    print('---------------------------')
    # print the current inventory
    print(f'Inventory : {str(inventory)}')
    print("---------------------------")

# Establishes code for dice game
def dice():

    player = 0
    monster = 0
    gameRound = 0

    while gameRound < 5:
        min = 1
        max = 6
        pt = 0
        mt = 0


        # Player roll
        print('Rolling the dice...')
        px = random.randint(min, max)
        py = random.randint(min, max)

        print(f'\nYou rolled a {px} and a {py}\n')
        # monster roll
        print('Rolling the dice...')
        mx = random.randint(min, max)
        my = random.randint(min, max)
        print(f'\nThe Spectre rolled a {mx} and a {my}\n')

        ps = px + py
        ms = mx + my

        if px == py or ps == 11 or ps == 7:
            pt += 1
        if mx == my or ms == 11 or ms == 7:
            mt += 1

        # if theres a tie or no points scored
        if pt == 1 and mt == 1:
            print('\nTie, lets roll again!\n')
            time.sleep(3)
            gameRound += 1
        elif pt == 0 and mt == 0:
            print('\nNeither got a point, roll again!\n')
            time.sleep(3)
            gameRound += 1

        # if the monster wins
        if mt == 1 and pt == 0:
            monster += 1
            print('\nI win this round\n')
            gameRound += 1
            time.sleep(3)

        # if the player wins
        elif pt == 1 and mt == 0:
            player += 1
            print('\nYou win this round\n')
            gameRound += 1
            time.sleep(3)



        if gameRound == 5:
            # prints current point standing
            print('\nYou have ' + str(player) + ' points and Spectre has ' + str(monster) + ' points.\n')
            if int(player) > int(monster):
                print('\nYou got the most points out of 5 rolls, you win fair and square.\nI\'ll leave this place but theres still a chance that your soul will be mine if you fail to escape this place.\nBefore the Spectre fades away he sets single red apple on the table and says\'Consider this a reward for a game well played\"!\n')
                time.sleep(5)
            elif int(player) < int(monster):
                print('I got the most points out of 5 rolls.\nYou\'re soul is mine.\n You feel yourself fading as the monster drag you to the depths of darkness\n\n GAME OVER!!!\n\n')
                time.sleep(5)
                exit()
            elif int(monster) and int(player) == 0:
                print('\nNo winner there so let\'s play again\n')
                time.sleep(5)
                dice()
            elif int(monster) == int(player):
                print('\nNo winner there so let\'s play again\n')
                time.sleep(5)
                dice()





def safecrack():
    while True:
        combo1 = input('Enter the first combination:\n')
        if int(combo1) == assets.safe_combo1:
            print('That\'s correct!')
        else:
            print('That\'s incorrect. Go back and find the clues again.')
            break
        combo2 = input('Enter the second combination:\n')
        if int(combo2) == assets.safe_combo2:
            print('That\'s correct!')
        else:
            print('That\'s incorrect. Go back and find the clues again.')
            break
        combo3 = input('Enter the third combination:\n')
        if int(combo3) == assets.safe_combo3:
            print('That\'s correct! Congratulations, you\'ve entered the combination correctly.\nYou now have the deathnote the one thing needed to escape this nightmarish home...')
            assets.rooms[currentRoom]['item'] = 'notebook'
            del assets.rooms[currentRoom]['container']
            break
        else:
            print('That\'s incorrect. Go back and find the clues again.')
            break


showInstructions()



# loop forever


while True:

    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into a list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go

        if move[1] in assets.rooms[currentRoom]:
            previousRoom = currentRoom
            currentRoom = assets.rooms[currentRoom][move[1]]
            # set the current room to the new room if user has required entry item or no item is required
            if 'ereq' in assets.rooms[currentRoom]:
                if assets.rooms[currentRoom]['ereq'] in inventory:
                    if 'gamestatus' in assets.rooms[currentRoom]:
                        print(assets.rooms[currentRoom]['desc'])
                        print('You\'ve won your freedom and quickly run from the home with the notebook in hand and a new friend in tow.\nAs the Shinigami lauchs meniacly you realize the nightmare may have just begun!!\nGAME OVER!!!')
                        exit()
                    else:
                        inventory.remove(assets.rooms[currentRoom]['ereq'])
                        del assets.rooms[currentRoom]['ereq']
                        time.sleep(3)


            #set room as previous room if entry requirement not met
                else:
                    print(assets.rooms[currentRoom]['efail'])
                    currentRoom = previousRoom
                    previousRoom = ''
                    time.sleep(3)


        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    if 'mons' in assets.rooms[currentRoom]:
        if assets.rooms[currentRoom]['mons'] is None:
            pass
        else:
            print(assets.rooms[currentRoom]['esuccess'])
            del assets.rooms[currentRoom]['mons']
            if 'game' in assets.rooms[currentRoom]:
                if assets.rooms[currentRoom]['game'] == 'dice':
                    # currentRoom = assets.rooms[currentRoom][move[1]]
                    time.sleep(5)
                    dice()


    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in assets.rooms[currentRoom] and move[1] in assets.rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del assets.rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'open' first
    if move[0] == 'open':
        # if the room contains an item, and the item is the one they want to get
        if "open" in assets.rooms[currentRoom] and move[1] in assets.rooms[currentRoom]['container']:
            if 'creq' in assets.rooms[currentRoom]:
                if assets.rooms[currentRoom]['creq'] == 'safecrack':
                    time.sleep(5)
                    safecrack()
        else:
            # tell them they can't get it
            print('Can\'t open ' + move[1] + '!')


