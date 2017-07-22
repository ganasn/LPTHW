# Exercise 30 - Else and If

people = 30
cars = 40
buses = 15

if cars > people:
    print "we should take the cars."
elif cars < people:
    print "we should not take the cars."
else:
    #invoked when cars == people
    print "we can't decide"
    
if buses > cars:
    print "too many buses."
elif buses < cars:
    print "maybe take the buses"
else: 
    print "we can't decide as they're the same number"
            
if people > buses:
    print "alright, we can take the buses."
else:
    print "fine, let's stay home"