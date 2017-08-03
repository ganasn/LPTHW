# Exercise 18 - Self-Study Drill
# How to assess the number of arguments passed with *args
from sys import argv

def count_args(*args):
    print len(args) #Always prints "1"
    print args[0] # Always prints the entire command line past "python"
    
count_args(argv)