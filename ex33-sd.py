# Exercise 33 Study-Drill on While-Loops
# Execute append in a function

numbers = []

def append_elements(counter): 
    count = 0
    while count < counter:
        print "At the top count is %d" % count
        numbers.append(count)
        count += 1
        print "List is", numbers
        print "At the bottom, count is %d" % count
    return 0

append_elements(int(raw_input('Enter # of elements to insert:')))
        
print "Numbers list is:" 
for tmp_count in numbers:
    print tmp_count