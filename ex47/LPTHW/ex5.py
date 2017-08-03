#Exercise #5 - More Variables & Printing

name = "Z.A.S"
age = 35
height = 74
weight = 150
eyes = "Brown"
teeth = "White"
hair = "Black"

print "Let's talk about %s." % name
print "They are %d inches tall." %height
print "They're %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "They've got %s eyes and %s hair." % (eyes, hair)
print "Their teeth are usually %s depending on the coffee." % teeth

#let's see if this is truly tricky
print "If one adds %d, %d, & %d, they'd get %d." %(age, height, weight, age + height + weight)
