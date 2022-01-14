#!/usr/bin/python3
'''Author: Chad Feeser, Contributor: James Freeman, Description: Quick walkthrough run of code for TLG Python course.'''

import time


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #inserts room description from dictionary
    print(f"{rooms[currentRoom]['desc']}")
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if "mons" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['mons'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'north': 'Kitchen',
        'south': 'Garden',
        'east': 'Dining Room',
        'west': 'Bedroom',
        'desc': 'It is dark and dismal with an intense sense of foreboding driving and an immense desire in you to escape as quickly as possible.!',
    },

    'Kitchen': {
        'south': 'Hall',
        'item':  'key',
        'desc': 'There are pots and dishes strewn across the room and blood splatters all over the walls.\nOn one of the walls is the numebr 242 hastely written in blood.',
    },
    'Dining Room': {
        'west': 'Hall',
        'item': 'apple',
        'desc': 'You surprised by the fact that the dining room is immaculate.\nThe table has been expertly set for an evening of fine dining except.\nThe only blemish you see is the number 161 carved into the table',
    },
    'Bedroom': {
        'east': 'Hall',
        'mons': 'Shinigami',
        'item': 'notepad',
        'desc': 'The room is disheveled and wreaks of death and sorrow.\nThe ticking of the grandfather clock send a chill up you spine.\nYou then notice the clocks hands are stuck on 3:25.',
    },
    'Garden': {
        'desc': "The door breaks free and you step out of the house just as the sun begins to rise."
    },
}


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
    #check for Dining room entry requirements
    if currentRoom == "Dining Room" and 'key' not in inventory:
        print('The door is lock up tight. You need to find a key!')
        currentRoom = "Hall"
        time.sleep(3)
    # Prevent user from trying to leave game before requirements are met
    if currentRoom == 'Garden' and 'notepad' not in inventory:
        print('You\'re can\'t leave until you\'ve found the nota mortum.')
        currentRoom = 'Hall'
        time.sleep(3)
    # check for Bedroom entry requirements and force user out if not met
    if currentRoom == "Bedroom" and 'mons' in rooms[currentRoom] and 'apple' not in inventory:
        print('You\'re suddenly forced out of the room by a Shinigami. It say\'s don\'t come back until you have something I\'ll like')
        currentRoom = "Hall"
        time.sleep(3)

    ##check for bedroom entry requirements and apply inventory and room changes as required
    if currentRoom == 'Bedroom' and 'apple' in inventory and 'Shinigami' in rooms[currentRoom]['mons']:
        print('The Shinigami say\'s, \"Oh you brought me an apple. I guess we could be friends so long as you keep bringing me these red delicaies.\"')
        del rooms[currentRoom]['mons']
        inventory.remove("apple")
        time.sleep(3)


    # Define how a player can win
    if currentRoom == 'Garden' and 'notepad' in inventory:
        print('\nYou\'ve escaped the house with the notepad and a new friend!!!... YOU WIN!\n')
        time.sleep(5)
        exit()

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
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
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')


    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1].lower() in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

