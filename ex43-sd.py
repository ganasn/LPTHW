#Exercise 43 - Classes

from sys import exit
from random import randint

#Exercise 43 - Classes

class Scene(object):
    def enter(self):
        print 'We\'ll be sub-classing the s**t out of this class'
        exit(1)
#        pass
    
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
#        pass

    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
#        pass
    

#Class Death of type Scene is one of the ways that this game ends
class Death(Scene):
#    List variable to hold what Death says once entering that scene
    death_says = [
        'You\'re finally here!',
        'I\'m the overlord, bow before me and accept your defeat.',
        'Your best was left swirling in the bowl earlier today, isn\'t it?',
        'You\'re not very good at this... go make me a sandwich.'
    ]
    
#    Member function that invokes Death's response upon entering
    def enter(self):
        print self.death_says[randint(0,len(self.death_says)-1)]
        exit(1)

#Class CentralCorridor of type Scene is where the game begins. enter() should be called to invoke the game
class CentralCorridor(Scene):
    
    def enter(self):
        print 'Long long ago, but somehow in the future...'
        print 'This could be a very boring game, and your objective is to follow someone else\'s thought process.'
        print 'As much as you\'d want to understand this...'
        print '...this is starting to annoy because there isn\'t any reference to a picture that might make this easier'
        print 'words, words, words.... followed by even more words...'
        print 'yes, I chose this myself and no one forced this upon me...'
        print 'nevertheless, I wouldn\'t quit my whining'
        
        print 'Your action choices are - shoot, dodge, or mokkai'
        action = raw_input('>')
        
        if action == 'shoot':
            print 'Something, something, dark side...'
            print 'You die..., everybody dies'
            return 'death'
        
        elif action == 'dodge':
            print 'terms of endearment'
            print 'brige of spies'
            print 'this just goes to show how much I care about this script'
            return 'death'
        
        elif action == 'mokkai':
            print 'this would probably the only way this code would flow to something that wouldn\'t terminate immediately'
            return 'laser_weapon_armory'
        
        else:
            print 'You didn\'t choose any of those 3'
            print 'Glad to know you don\'t partake in these vagaries'
            print 'But you go back and do this all over!'
            return 'central_corridor'
        
#        pass
    
#Class LaserWeaponArmory that is of type Scene that will be one of the stops from Central Corridor
class LaserWeaponArmory(Scene):
#    Invoked from Central Corridor with mokkai
    def enter(self):
        
#        Interestingly, this is a string... I didn't realize that
#        code = '%d%d' % (randint(1,2), randint(1,2))
        code = randint(10,99)
        guesses_allowed = 3
        guess = 0
        guesses = 0
        
        print 'code %d' % code
        print 'You in LaserWeaponArmory.enter()'
        print 'Guess the 2 digit code in %d guesses to move on' % guesses_allowed
        
        while guess != code and guesses <  guesses_allowed:
            try:
                guess = int(raw_input('Code is... >'))
            except ValueError:
                print 'That wasn\'t a number... do that again'
                pass
#            if guesses_allowed > 1: 
#                print 'Wrong guess, try again'
            guesses += 1
            
        if guess == code:
            print 'moving onto the bridge'
            return 'the_bridge'
        else:
            print 'death at laser armory'
            return 'death'
            
#        pass
    
#Class Bridge of type Scene, invoked from LaserArmory to bomb the crap out of this...
class TheBridge(Scene):
    
#    Three options - 1 to death, another to the bridge (w/ these same steps,) and another to escape pod
    def enter(self):
        print 'You gots the bomb under your arm'
        print 'You get 2 more choices - throw or place'
        action = raw_input('throw or place >')
        if action == 'throw':
            print 'thank you for throwing the bomb'
            print 'you die and end this misery'
            return 'death'
        elif action == 'place':
            print 'good for you... you placed it and will continue this misery'
            return 'escape_pod'
        else:
            print 'well, you gotta do this again because apparently you don\'t know how to type'
            return 'the_bridge'
#        pass

#Class EscapePod of type Scene - one more guessing game
class EscapePod(Scene):

    #    Two choices with 1 guess - either go to death or win. With that, this also becomes one of the exit points
    def enter(self):
        
        code = randint(1,5)
        guesses_allowed = 1
        guesses = 0
        guess = 0
        
        print 'Good pod guess is %d' % code
        print 'You get %d guess(es)' % guesses_allowed
        
        while guess != code and guesses <  guesses_allowed:
            try:
                guess = int(raw_input('Code is... >'))
            except ValueError:
                print 'That wasn\'t a number... do that again'
                pass
            print 'Wrong guess, try again'
            guesses += 1
            
        if guess == code:
            print 'you win\n\n\n\n\n'
#            Using return 'central_corridor' will keep looping the game
#            return 'central_corridor'
            return 'finished'
        else:
            print 'death at escape pod'
            return 'death'
        
#        pass
    

#Adding class Finished of type Scene to not route it back to CentralCorridor. This would just terminate the program gracefully instead of abending. 
#A try-except block might work too! 
class Finished(Scene):
    def enter(self):
        print 'In Finished.self()'
        exit(0)

class Map():
    
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
#        pass
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
#        pass
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
#        pass
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()