#Exercise 47 - Automating Tests

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        return 0
        
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)