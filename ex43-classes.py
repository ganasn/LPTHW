#Exercise 43 - Classes
#This is a skeleton set of classes

#This will be inherited 
class Scene(object):
    def enter(self):
        pass

#Actual controller of the game
class Engine(object):
    def __init__(self, scene_map):
        pass
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
#        pass
    
#one of two exit points of the game
class Death(object):
    def enter(self):
        print 'in Death.enter()'
        pass
    
#game's starting point - scene 1
class CentralCorridor(Scene):
    def enter(self):
        print 'in CentralCorridor.enter()'
        pass
    
#one of the scenes on happy path - scene #3
class LaserWeaponArmory(Scene):
    def enter(self):
        print 'in LaserWeaponArmory.self()'
        pass

#scene 2 on happy path
class TheBridge(Scene):
    def enter(self):
        print 'in TheBridge.self()'
        pass
    
#scene 4 on happy path - another exit point for the game
class EscapePod(Scene):
    def enter(self):
        pass
    
class Map():
    def __init__(self, start_scene):
        pass
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()