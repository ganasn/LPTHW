#Exercise 44 - Inheritance v Composition
#Accessing parent qualities inside child class

class Parent(object):
    
    def altered(self):
        print 'Parent altered()'

class Child(Parent):
    def altered(self):
        print 'Child, Before Parent altered()'
        super(Child,self).altered() #This is the call to Parent.altered()
        print 'Child, After Parent altered()'
        

dad = Parent()
son = Child()

dad.altered()
son.altered()