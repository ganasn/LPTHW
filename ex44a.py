#Exercise 44 - Inheritance v Composition
#Implicit Inheritance - a function is defined in the parent class but NOT in the child class

class Parent(object):
    
    def implicit(self):
        print 'Parent implicit()'

class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()