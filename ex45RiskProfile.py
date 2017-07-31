#Exercise 45 - The Game
#Risk Profile class

import ex45Portfolio

class RiskProfile(object):

    PORTFOLIO_MIX = {
        '1':'conservative',
        '2':'moderate',
        '3':'aggressive'
    }
    
    def __init__(self):
#        risk_profile = 0
        pass
        
    def allocate(self, current_age, retirement_age):
        print 'You plan to retire in %d years' % (retirement_age - current_age)
#        functionality to be defined later
#        if diff is < 10, then mix is 1, if 10 < diff < 15 then moderate, else conservative
#        pass
        
    