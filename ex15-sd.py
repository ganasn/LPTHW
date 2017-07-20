# Exercise 15 - Study Drill 
# Attempt to send file name via another file name - so you edit the config file without having to provide data file name every time
# alternatively, the config file name can be hardcoded for production environments

from sys import argv

script, conffile = argv

# Without any regard to handling exceptions here

configfile = open(conffile) #configfile is a file object & conffile is a string
datafile = configfile.read()  #datafile is a string object
data = open(datafile) #data is a file object
print "data from data file %r that was from %r config file is: " % (datafile, configfile)
print data.read()

configfile.close()
data.close() 


# how to close the file that was opened?
# both close statements above throw error as they're considered strings