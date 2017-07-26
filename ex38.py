# Exercise 38 - Doing Things to Lists

ten_things = 'Apples Oranges Crows Phone Light Sugar'

print 'That doesn\'t add to 10'

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# Add more items to stuff from more_stuff until there are 10 items in stuff
#Stuff would initially have 6 - from ten_things
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print 'Adding', next_one
#    adding to the end of list <stuff>
    stuff.append(next_one)
    print 'There are %d items now' % len(stuff)
    
print 'Now it\'s done:', stuff

print 'More ops with <stuff> variable'

#get second item
print stuff[1]
#get last item
print stuff[-1]
#move first item off stuff. stuff doesn't have 10 items any longer
#this is the last item - LIFO - not the first item
print stuff.pop()
#trying pop(<ordinal>)
print stuff.pop(1)
#Adds stuff to a another string which is just ''
#That was obviously incorrect. This actually joins the items in stuff list with the string ''
#print ''.join(stuff)
print ' '.join(stuff)
#Adds elements 4 through 6 (or 5?) from stuff to a string that's '#'
#As expected, only 2 elements are considered - the last element is NOT considered
#From previous line, this would join elements 4 & 5 with a '#'
print '#'.join(stuff[3:5])