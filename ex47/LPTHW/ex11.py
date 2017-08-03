# Exercise 11 - Asking Questions

print "How old are you?" # notice that this does NOT have a comma that leads to inputs keyed on a NEW line as the text printed
age = raw_input()  # capturing user input and persisting in variable named 'age'
print "How tall are you?"
height = raw_input()
print "How much do you weigh?", # notice that this has a comma that leads to inputs keyed on the same line as the text printed
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)