# Exercise 17 - More Files
# Copy one file into another

from sys import argv
from os.path import exists

script, src_file, tgt_file = argv

print "Copying from %s to %s" %(src_file, tgt_file)

indata = open(src_file).read() # given that this is string now, was the file object even created? If yes, how do I close it? 
# Apparently file object is NOT created and hence Python auto-closes it once this line is executed

print "Input file is %d bytes long" % len(indata)

print "Checking if output file exists: %r" % exists(tgt_file)

# It does not seem like multiple modes can be combined here
# This also creates the file if the tgt_file does not exist
out_file = open(tgt_file, 'a')
out_file.write("\n" + indata)
out_file.close()

print "Copied over"
# Following line will NOT work as the file is open in append mode and NOT for read mode
# print "\nTarget file after append process is: %s" % out_file.read()

print "\n Target file after append process is: %s" % open(tgt_file).read()

# out_file.close() ## Moved immediately after .write()
