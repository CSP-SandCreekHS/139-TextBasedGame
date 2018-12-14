from __future__ import print_function
import random
#Below is where the lists will be held, all will be empty at the beggining

items = []
entered_rooms = []
opened_doors = []

def startGame():
    print('Greetings traveler! Hidden in this dungeon is a diamond, you must find it!')
    input('press enter to begin')
    room1()

def room1():  #this is the funtion that happens after enter is pressed
    global items
    global entered_rooms # this allows us to put data into these throughout the funtion
    global opened_doors
    exitroom = False #this shows us that we have not left the room1 yet
    floorbox1 = ['notepad1','key'] #this puts a list of strings into the box so the player may pick them up
    cabinet = ['lanturn']
    print('Ah you found youreself into the first room')
    print('there is a door straight infront of you (door1),a door to the right (door2), a box1 on the floor, and a cabinet. ')
    useraction = input('What do you wish to do? ') #this sets the user action as a string so we can use the input later
    while exitroom == False: #everything that happens before you exit the room
        if useraction == 'open door1' and 'lanturn' in items: # this checks your inventory for the item and if you have it you proceed
            print('The door opens and the lanturn shows 2 more doors. ')
            opened_doors += ['door1']
            entered_rooms += ['room2']
            exitroom = True
        elif useraction == 'open door2' and 'key' in items:
            print('the key unlocks the door and you creek it open. revealing 2 more doors')
            opened_doors += ['door2']
            entered_rooms += ['room3']
            exitroom = True
        elif useraction == 'open box1':
            print('You picked up', floorbox1)
            items += floorbox1 #this transfers the box items into you inventory
            floorbox1 == [] #this empties the box's items
            print('open door1, open door2, open cabinet, open box1')
            useraction = input('what would you like to do now? ')
        elif useraction == 'open cabinet':
            print('You picked up', cabinet)
            items += cabinet #this transfers the cabinet items into you inventory
            floorbox1 == [] #this empties the cabinet's items
            print('open door1, open door2, open box1')
            useraction = input('what would you like to do now? ')
        elif useraction == 'open door1' and 'lanturn' not in items:
            print('the room is too dark to enter, you close the door')
            print('open door1, open door2, open cabinet, open box1')
            useraction = input('what would you like to do now? ')
        elif useraction == 'open door2' and 'key' not in items:
            print('the door is locked you need to find a key. ')
            print('open door1, open door2, open cabinet, open box1')
            useraction = input('what would you like to do now? ')
        elif useraction == 'open box1' and 'notepad' in items:#these next two commands are so you cannot open the same thing twice
            print('you have already searched this box')
            print('open door1, open door2, open cabinet, open box1')
            useraction = input('what would you like to do now? ')
        elif useraction == 'open cabinet' and 'lanturn' in items:
            print('you have already searched this cabinet')
            print('open door1, open door2, open cabinet, open box1  ')
            useraction = input('what would you like to do now? ')
        else:
            useraction = input('not a valid action, try again. ') #if user types something wrong they get this message
    if 'door1' in opened_doors:
        room2()
    else:
        room3()
        
def room2():
    global items
    global entered_rooms
    global opened_doors
    exitroom2 = False #this shows us that we have not left the room2 yet
    print('you have entered room2 and the lanturn illuminates it. ')
    print('there is a door to the left of you (door3),a door to the right (door4), a 3 moving pillars with patters on them. ')
    useraction = input('What do you wish to do? ') #this sets the user action as a string so we can use the input later
    while exitroom2 == False:
        if useraction == 'open door3' and 'working combo' in items:
            print('you move the pillars into the correct spot and the door opens ')
            opened_doors += ['door3'] #this adds the variable into the list
            entered_rooms += ['room5']
            exitroom2 = True
        elif useraction == 'open door4' and 'key' in items:
            print('the key unlocks the door and you creek it open. ')
            opened_doors += ['door4']
            entered_rooms += ['room4']
            exitroom2 = True
        elif useraction == 'open door3' and 'working combo' not in items:
            print('Nothing happens, wrong combo. ')
            print('open door3, open door4, move pillars. exit room ')
            useraction = input('what would you like to do now? ')
        elif useraction == 'open door4' and 'key' not in items:
            print('the door is locked you need to find a key. ')
            print('open door3, open door4, move pillars. exit room ')
            useraction = input('what would you like to do now? ')
        elif useraction == 'exit room':
            room1()
        else:
            useraction = input('not a valid action, try again. ')
    if 'door3' in opened_doors:
        room5()
    else:
        room4()

def room3():
    global items
    global entered_rooms
    global opened_doors
    exitroom3 = False #this shows us that we have not left the room3 yet
    print('Ah you found youreself into the third room')
    print('there is a door to the left (door5),a door to the right (door6). ')
    useraction = input('What do you wish to do? ') #this sets the user action as a string so we can use the input later
    while exitroom3 == False:
        if useraction == 'open door5':
            print('The door opens and you walk through ')
            opened_doors += ['door5']
            entered_rooms += ['room4']
            exitroom3 = True
        elif useraction == 'open door6' and 'bomb' in items:
            print('the bomb blows up a door and you walk through it. ')
            opened_doors += ['door6']
            entered_rooms += ['room6']
            exitroom3 = True
        elif useraction == 'open door6' and 'bomb' not in items:
            print('the door wont budge and there no way to open it')
            print('open door5, open door6. exit room ')
            useraction = input('what would you like to do now? ')
        elif useraction == 'exit room':
            exitroom3 = True
            room1()
        else:
            useraction = input('not a valid action, try again. ')
    if 'door6' in opened_doors:
        room6()
    else:
        room4()

def room4():
    global items
    global entered_rooms
    global opened_doors
    exitroom4 = False #this shows us that we have not left the room4 yet
    statue = ['used notepad']
    print('You have entered room 4')
    print('there is a door to the left (door4), and 3 odd statues ')
    useraction = input('What do you wish to do? investigate statues or open door 4 ') #this sets the user action as a string so we can use the input later
    while exitroom4 == False:
        if useraction == 'open door4':
            print('The door opens and you walk through ')
            opened_doors += ['door4']
            entered_rooms += ['room2']
            exitroom4 = True
        elif useraction == 'investigate statues' and 'notepad1' in items:
            print('you sketch down the design into your notepad. now you have ', statue)
            items += statue
            useraction = input('what would you like to do now? open door4 ')
        elif useraction == 'investigate statues' and 'notepad1' not in items:
            print('you dont seem to have anything to write these down onto. ')
            useraction = input('what would you like to do now? investigate statue, open door4, exit room')
        elif useraction == 'exit room':
            exitroom4 = True
            room3()
        else:
            useraction = input('not a valid action, try again. ')
    if 'door4' in opened_doors:
        room2()

def room5():
    global items
    global entered_rooms
    global opened_doors
    exitroom5 = False #this shows us that we have not left the room5 yet
    bomb = ['bomb']
    print('you have entered room5. ')
    print('the only thing in here seems to be some kine of bomb. ')
    useraction = input('What do you wish to do? pickup bomb, exit room. ') #this sets the user action as a string so we can use the input later
    while exitroom5 == False:
        if useraction == 'pickup bomb':
            print('you have picked up the ', bomb)
            items += bomb
            useraction == input('what would you like to do now? pickup bomb, exit room ')
        elif useraction == 'pickup bomb' and 'bomb' in items:
            print('you have already picked up the bomb ')
            useraction = input('what would you like to do now? exit room, pickup bomb ')
        elif useraction == 'exit room':
            room2()
        else:
            useraction = input('not a valid action, try again. ')

def room6():
    global items
    global entered_rooms
    global opened_doors
    exitroom6 = False #this shows us that we have not left the room6 yet
    prize = ['diamond']
    print('you have entered room6. ')
    print('it looks like this is the last chamber. theres a diamond in the room.  ')
    useraction = input('What do you wish to do? pickup diamond, exit room. ') #this sets the user action as a string so we can use the input later
    while exitroom6 == False:
        if useraction == 'pickup diamond':
            print('you have picked up the ', prize)
            items += prize
            print('Congradulations! you have beat the game')
            endgame()
        elif useraction == 'exit room':
            room3()
        else:
            useraction = input('not a valid action, try again. ')

def endgame():#this funtion plays at the end of the game
    print('you have collected',items) # these tell you what you have done through the game
    print('you have entered', entered_rooms)
    print('you have opened', opened_doors)
    useraction = input('would you like to play again? play again')
    if useraction == 'play again': # this will replay the game if the user types "play again"
        room1()
    else:
        print('goodbye')