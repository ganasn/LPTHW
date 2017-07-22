#ex25.py
#Exercise 25 - Even More Practice

#Return words array from a string argument passed
def break_words(stuff):
    words = stuff.split(' ')
    return words

#Sorts an array of words passed to it
def sort_words(words):
    return sorted(words)

#Pop the first word of an array passed and print that word
def print_first_word(words):
    word = words.pop(0)
    print word
    
#Pop the last word of an array passed and print that word
def print_last_word(words):
    word = words.pop(-1)
    print word
    
#Pass a full sentence as a string, break it into words, and sort those words
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

#Print first and last word of a sentence
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
#Print first and last word of a sentence after sorting the words in that sentence
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

