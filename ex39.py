#Exercise 39 - Dictionaries

#Python calls these dicts and other languages call these hashes
#Dicts associate one thing to another

#Create a mapping of state to abbreviation

states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'Minnesota':'MN',
    'New York':'NY'
    }

#create a basic set of states and some cities in them
cities = {
    'CA':'Sacramento',
    'OR':'Eugene',
    'MN':'St. Paul',
    'NY':'Ithaca',
    'FL':'Tampa'
}

#adding few more cities
cities['WI'] = 'Madison'
cities['GA'] = 'Savannah'

print '-'*10
print 'Wisconsin state has:',cities['WI']

print '-'*10
print 'New York\'s abbreviation is:', states['New York']

print '-'*10
#Following 2 lines fail because the key does not match those in the dict AKA container
#print 'California has:', cities[states['california']]
#print 'Oregon has:',cities[states['ORegon']]
print 'California has:', cities[states['California']]
print 'Oregon has:',cities[states['Oregon']]

print '-'*10
#given that it's a name-value pair, there are 2 items coming from the dict
for abbrev, city in cities.items(): 
    print '%s has the city %s' % (abbrev, city)
    
print '-'*10
for state, abbrev in states.items():
    print '%s state is abbreviated %s and has the city %s' % (state, abbrev, cities[abbrev])
    
print '-'*10
state = states.get('Texas', None)

if not state:
    print 'Texas wasn\'t on the list'
    
city = cities.get('TX','Does Not Exist')
print 'The city for the state of \'TX\'is %s' % city