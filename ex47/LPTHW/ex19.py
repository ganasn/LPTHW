# Exercise 19 - Functions & Variables
# To prove that variables used while calling functions and that used by said-called-functions are different

def cheese_cracker(cheese_count, cracker_count):
    print "You have %d cheeses & %d boxes of crackers \n" %(cheese_count, cracker_count)
    
print "Giving numbers directly"
cheese_cracker(10, 20)

# This must error out for type reasons - a number is expected and a string was received
# cheese_cracker("one","two")

print "Calling using same variable names"
cheese_count = 10
cracker_count = 20
# cheese_cracker(30, 40)
# print cheese_count, cracker_count
cheese_cracker(cheese_count, cracker_count)

print "Calling with math"
cheese_cracker(10-1, 20-2)
