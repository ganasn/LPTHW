# Exercise 21 - Functions can Return Something

def add_nums(first, second):
    print "Adding %d & %d gives: " %(first, second),
    return first + second

def sub_nums(first, second):
    print "Subtracting %d from %d gives: " %(second, first), 
    return first - second

first_num = int(raw_input("Enter first number: "))
second_num = int(raw_input("Enter second number: "))

print add_nums(first_num, second_num) # This call does NOT work if add_nums is defined beyond this point
print sub_nums(first_num, second_num)


