#Exercise 44 - Inheritance v Composition

class Other(object):
    
    def override(self):
        print 'OTHER override()'
        
    def implicit(self):
        print 'OTHER implicit()'
        
    def altered(self):
        print 'OTHER altered()'
        
class Child(object):
    
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print 'CHILD override()'
        
    def altered(self):
        print 'CHILD altered() before call to OTHER'
        self.other.altered()
        print 'CHILD altered() after call to OTHER'
        
other = Other()
child = Child()

#other.override()
child.override()
#other.altered()
child.altered()
#other.implicit()
child.implicit()