#Exercise 41 - Object Oriented
#Logic of convert() is unclear - it does NOT return 2 values as expected - instead, it only returns the 2nd value'phrase' passed 
#Code breaks at question,answer = convert(snippet,phrase)

import random
from urllib import urlopen
import sys

WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []

PHRASES = {
    'class %%%(%%%):':'Make a class named %%% that is-a %%%.',
    'class %%%(object):\n\tdef __init__(self, ***)': 'class %%% has-a __init__ that takes self and *** parameters.',
    'class %%%(object):\n\tdef ***(self,@@@)':'class %%% has-a function named *** that takes self and @@@ as parameters.',
    '*** = %%%()':'Set *** to an instance of the class %%%',
    '***.***(@@@)':'From *** get the *** function and call it with parameters @@@.',
    '***.*** = ***':'From *** get the *** attribute and set it to ***.'
}

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count('***'))
    results = []
    param_names = []
    
    for i in range(0, snippet.count('@@@')):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS, param_count)))

    print 'snippet from convert is %s\n' % snippet
    print 'phrase from convert is %s\n' % phrase
    for sentence in snippet,phrase: 
        print 'sentence is %s\n' % sentence
        result = sentence[:]
        
    print 'result immediately after instantiating is %r\n' % result
    
    for word in class_names:
        result = result.replace('%%%',word,1)
        
    print 'result after class_names replacements is %r\n' % result

    for word in other_names:
        result = result.replace('***',word,1)
        
    print 'result after other_names replacements is %r\n' % result
    
    for word in param_names:
        result = result.replace('@@@',word,1)
        
    print 'result after param_names replacements is %r\n' % result
        
    results.append(result)
    
    print 'result\'s\' after appending from \'result\' is %r\n' % results
    
    return results

#decide key or value
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
    
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

try:
#    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            print 'snippet is:%s\n' % snippet
            print 'phrase is:%s\n' % phrase
#            question = convert(snippet,phrase)
#Code breaks in this next line given that convert(x,y) returns only 1 value
            question,answer = convert(snippet,phrase)
            print 'question is %s\n:' % question
#            exit(0)
            if PHRASE_FIRST:
                question, answer = answer, question
                
            print question
            raw_input('>')
            print 'ANSWER: %s\n\n' % answer
except EOFError:
    print '\nBye'
    
