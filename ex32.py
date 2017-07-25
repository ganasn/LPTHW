# Exercise 32 - Loops & Lists
# Introducing for loop

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#reading from lists

for number in the_count:
    print 'This is count %d' % number
    
for fruit in fruits:
    print 'Fruit of type: %s' % fruit

for item in change:
    print "Item %r" % item
    
# Writing to lists
elements = []

for count in range(0,10):
    print "adding %d to elements" % count
    elements.append(count)
    
for count in elements:
    print "Element inserted was %d" % count
    