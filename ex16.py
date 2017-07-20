# Exercise 16 - Reading & Writing Files

from sys import argv

script, datafile = argv

#datafile is the string with file name

print "Do you want to erase %r?" % datafile
print "Press CTRL+C (^C) for NO."
print "Press RETURN for YES."

# What does the following line do? 
raw_input('?')

print "Opening target file"
target = open(datafile, 'w') #opening data file in write mode, without which truncate() will NOT work. target is the file object for playing

print "Truncating file %r" % datafile

target.truncate()

print "Now for inputs: "
line1 = raw_input("enter line 1: ")
line2 = raw_input("enter line 2: ")
line3 = raw_input("enter line 3: ")

print "writing lines to file %r" % datafile

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.close()

target = open(datafile, 'r') #opening data file in read mode. 
print "contents of %r " % datafile
print target.read()
target.close()