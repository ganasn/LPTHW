# Exercise 13 - Parameters, Unpacking, Variables

from sys import argv

# seems like we're taking 4 arguments, first of which is the file AKA script name, which in this case is ex13.py, and then 3 arguments to the script
script, first, second, third = argv

#not giving arguments other than script throws an error 

# Trying different kinds of print 
print "The script is called %r" % script
print "Your first variable is: ", first
print "Your second and third variables are %r & %r" % (second, third)
