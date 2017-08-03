print "I will now count my chickens"
print "Hens", 25+30/6 #30
print "Roosters" , 100 - 25 * 3 % 4 #Expression is multipleied before modulus is evaluated
#so, it is 100 - 75 % 4 = 100 - 3 = 97

print "Now I will count the eggs:"

# print 3.0-1/4 #this is NOT evaluated as 2.75, answer is still 3
# print 3.0-1.0/4#hopefully, this is evaluated as 2.75? yes, basically the floating point is triggered by division operation
# print 3 - 1/4.0#evaluated as 2.75
# print 3 - 1.0/4#evaluated as 2.75
# print 3 - 1 / 4 #this is evaluated as 3 - 0.25 = 2.75, converted back into integer as 3
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#evaluated as 6-5+0-0+6 = 7

print "Is it true that 3+2<5-7?"
print 3+2<5-7#false

print "What is 3+2?", 3+2#5
print "What is 5-7?", 5-7 #-2

print "Oh, that's why it's false"

print "How about some more."

print "Is it greater?",5>-2 #true
print "Is it greater or equal?", 5 >=-2 #true
print "Is it less or equal?", 5<=-2 #false
