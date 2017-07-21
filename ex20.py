# Exercise 20 - Functions & Files

from sys import argv

script, src_file_name = argv

# argument 'f' is a file object
def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_one_line(line_number, f):
    print line_number, f.readline()
    
src_file = open(src_file_name)

print "Printing whole file:\n",
print_all(src_file)

# Without the following block, print_one_line() that follows will NOT print anything - it does NOT throw an error either despite reaching EOF
print "Rewind the file like a tape"
rewind(src_file)

print "Printing few lines"
print_one_line(2000, src_file)
print_one_line(2001, src_file)
