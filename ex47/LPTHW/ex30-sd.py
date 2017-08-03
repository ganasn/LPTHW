# Exercise 30 - Else and If Study Drill

#people = 30
#cars = 40
#buses = 15

from sys import argv

script, people, cars, buses = argv

#if cars > people:
#    print "we should take the cars."
#elif cars < people:
#    print "we should not take the cars."
#else:
#    #invoked when cars == people
#    print "we can't decide"
#    
#if buses > cars:
#    print "too many buses."
#elif buses < cars:
#    print "maybe take the buses"
#else: 
#    print "we can't decide as they're the same number"
#            
#if people > buses:
#    print "alright, we can take the buses."
#else:
#    print "fine, let's stay home"


print "\n people %d cars %d buses %d\n\n\n\n\n\n" %(int(people), int(cars), int(buses))

people = int(people)
cars = int(cars)
buses = int(buses)

if people > buses and people > cars:
    print "maybe, the world is balanced"
elif people < cars:
    print "world has too many travel options - wasteful!!"
elif people > buses and people <= cars: 
    print "take the buses people!!"
else:
    print "mind the pollution!!"