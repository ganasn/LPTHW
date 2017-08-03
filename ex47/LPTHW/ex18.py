# Exercise 18 - Names, Variables, Code, & Functions

def two_args(*args):
    arg1, arg2 = args
    print "Unpacking 2 arguments - arg1: %r arg2: %r" % (arg1, arg2)

def pass_as_two(arg1, arg2):
    print "Passing as 2 arguments: arg1 is %r & arg2 is %r" % (arg1, arg2)
    
def one_args(arg1):
    print "One argument: %r" % arg1
    
def no_args():
    print "No arguments here"

# Following line throws the error that there are too mnay values to unpack
# two_args(1, 2, 3, 4)
two_args("two_args","two")
pass_as_two("pass_as_two", "one")
one_args("one_args")
# Following line throws the error that no_args() takes no arguments
# print no_args("no_args")
no_args()