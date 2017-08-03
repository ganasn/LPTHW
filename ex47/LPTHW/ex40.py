#Exercise 40 - Modules, Classes, & Objects

#Class Song that take a variable lyrics
class Song(object):
#    this is the constructor that assigns lyrics list passed upon instantiating the class
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
#    this is the member function of the class Song that its objects can call
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            

#This is an object of class Song that takes few lines of the song into member variable lyrics
happy_bday = Song(['Happy b\'day to you', 'Many girl\\boyfriends to you','And maybe your dreams will come true'])

bulls_on_parade = Song(['They rally \'round your family', 'With a pocket full of shells'])

#the following line to create an object must fail as this does not create a list
#interestingly this did NOT cause any issues, instead the string was broken into individual characters and printed out
toxicity = Song('Why don\'t you ask the kids at Tianamen Square')

#No outputs so far...

happy_bday.sing_me_a_song()
print '\n'*3
bulls_on_parade.sing_me_a_song()
print '\n'*3
toxicity.sing_me_a_song()