#Exercise 8 - Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#this last line formats strings with apostrophe by default and with quotes if the string already has apostrophe
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# what if I am missing one of the formatter inputs
# Python throws an error stating there aren't enough arguments
# print formatter % (1, 2, 3)