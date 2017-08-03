#Exercise 44 - Inheritance v Composition

class Parent(object):
    
    def override(self):
        print 'parent override()'
        
    def implicit(self):
        print 'parent implicit()'

    def altered(self):
        print 'parent altered()'
                
class Child(Parent):
    def override(self):
        print 'child override()'

    def altered(self):
        print 'child call of altered() before parent call'
        super(Child,self).altered()
        print 'child call of altered() after parent call'
                            
            
parent = Parent()
child = Child()

parent.implicit()
child.implicit()

parent.override()
child.override()

parent.altered()
child.altered()