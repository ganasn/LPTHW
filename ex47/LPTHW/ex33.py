# Exercise 33 - While-Loops
# To keep executing a loop as long as a Boolean expression is true

count = 0
numbers = []

while count < 6:
    print "At the top count is %d" % count
    numbers.append(count)
    count += 1
    print "List is", numbers
    print "At the bottom, count is %d" % count
    
print "Numbers list is:" 
for tmp_count in numbers:
    print tmp_count