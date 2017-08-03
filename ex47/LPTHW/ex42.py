#Exercise 42 - Is-A, Has-A, Objects, & Classes

#Animal is-a object 
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
#        constructor that takes self and name passed to create object of class Dog
        self.name = name
    
#Another class Cat that is-a Animal
class Cat(Animal):

    def __init__(self, name):
#        constructor that takes self and name passed to create object of class Dog
        self.name = name

#class named Person that inherits from class 'object'
class Person(object):
    
#    Constructor that takes self and name as parameters to assign member variables name & pet (to None)
    def __init__(self, name):
        self.name = name
        self.pet = None
        
#class Employee that is-a Person
class Employee(Person):
#    constructor of class Employee that takes name & salary as parameters
    def __init__(self, name, salary):
#        calls __init__() of class Person with the name value passed to it
        super(Employee,self).__init__(name)
    
#class Fish that is-a Object
class Fish(object):
    pass

#class Salmon that is-a Fish
class Salmon(Fish):
    pass

#class Halibut that is-a Fish
class Halibut(Fish):
    pass

#object of class Dog w/ name value equals 'rover'
rover=Dog('rover')

#objec of class Cat w/ name value equals 'billi'
billi = Cat('billi')

mary = Person('mary')

mary.pet = billi

frank = Employee('Frank',10000)
frank.pet = rover

#objects with no name values
flipper = Fish()
crouse = Salmon()
harry = Halibut()

print 'frank is %r\n' % frank