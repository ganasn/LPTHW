#Exercise 35 - Branches & Functions
#Reviewing all coding blocks learned until now

from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input('>')
    if "0" in next or "1" in next:
        how_much = int(next)
    else: 
        dead('Learn to type a number')
    
    if how_much < 50:
        print 'You\'re not greedy'
        exit(0)
    else:
        dead('You\'re greedy')
    
def bear_room():
    print 'There is a bear here.'
    print 'The bear has honey.'
    print 'The fat bear is in front of another door.'
    print 'How\'re you going to move the bear?'
    bear_moved = False
    
    while True:
        next = raw_input('>')
        if next == 'take honey':
            dead('Bear slaps your face off')
        elif next == 'taunt bear' and not bear_moved: #'not' bear_moved seems incorrect - since bear_moved = False means that the bear didn't move
            print 'Bear has moved. Go thru\''
        elif next == 'taunt bear' and bear_moved:
            dead('Bear is pissed off and mauls you')
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print 'Unsure what you mean'
    return 0

def cthulhu_room():
    print 'Here, you encounter the worst in you'
    print 'It makes you insane'
    print 'Do you fight or flee?'
    
    next = raw_input('>')
    
    if 'flee' in next:
        start()
    elif 'fight' in next:
        dead('bad choice')
    else:
        cthulhu_room()
    return 0

def dead(reason):
    print reason, 'Great!'
    exit(0)
    
def start():
    print 'You\'re in a dark room'
    print 'There is a door to your right and left'
    print 'Which one do you open?'
    
    next = raw_input('>')
    
    if next == 'left':
        bear_room()
    elif next == 'right':
        cthulhu_room()
    else:
        dead('You\'ll starve to death')
    exit(0)
    
start()
            
