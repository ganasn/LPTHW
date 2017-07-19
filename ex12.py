# Exercise 12 - Prompting People

# Changing print <question> & raw_input() into raw_input(<question>)

# For print to print this as %d, this needs to be converted into int(). Without int() it'd treat even a number entered as a string
age = int(raw_input("How old are you?"))
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

# No comma between print & variables
print "So, you're %d old, %r tall, & %r heavy." % (age, height, weight)

# Comma between print & variables - this throws an error
# print "So, you're %d old, %r tall, & %r heavy.", % (age, height, weight)