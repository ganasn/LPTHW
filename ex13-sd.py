# Exercise 13 - Study Drill
# Exercise 13 - Parameters, Unpacking, Variables

from sys import argv

# seems like we're taking 4 arguments, first of which is the file AKA script name, which in this case is ex13.py, and then 3 arguments to the script
script, first, second, third = argv
# not giving arguments other than script throws an error 

# requesting a 4th input
# fourth = raw_input("Give me one more argument:")

# Trying different kinds of print 
print "The script is called %r" % script
print "Your first variable is: ", first
print "Your second and third variables are %r & %r" % (second, third)

# requesting a 4th input & testing if the order of print & raw_input() matter
# using fourth again does NOT seem to be an issue, although good programming practice must call it something else
fourth = raw_input("Give me one more argument after printing first 3 args:")

print "And the script itself asked for the fourth: %r" % fourth
