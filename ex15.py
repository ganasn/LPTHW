# Exercise 15 - Reading Files 

from sys import argv

script, filename = argv

txt = open(filename)

print "Output from %r: " % filename
print txt.read()

# how to close the file that was opened?
# close the object that was assigned the open() 
txt.close()

# This can be potentially looped in and read different (or same) files