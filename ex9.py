# Exercise 9 - Printing, Printing, Printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\nSep\nOct\nNov\nDec"
#introducing \n, the new line escape sequence, introduces new lines while printing

print "Here are the days:", days
print "Here are the months:", months
print "Here are the months with raw formatter: %r" % months

print """
    There's something going on here.
    With the three quotes.
    We'll be able to type as much as we like.
    Even 4 lines if ew want, or 5, or 6.
    """
