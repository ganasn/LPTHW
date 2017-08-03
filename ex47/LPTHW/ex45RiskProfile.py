#Exercise 45 - The Game
#Risk Profile class

import ex45Portfolio

class RiskProfile(object):
#For some reason, this does NOT compute as a global variable
#    PORTFOLIO_MIX = {
#        '1':'conservative',
#        '2':'moderate',
#        '3':'aggressive'
#    }

    
    stocks = 0
    bonds = 0
    
    def __init__(self):
#        risk_profile = 0
        pass
        
    def allocate(self, current_age, retirement_age):
        
        PORTFOLIO_MIX = {
            '1':'conservative',
            '2':'moderate',
            '3':'aggressive'
        }
        
        diff = retirement_age - current_age
        print 'You plan to retire in %d years' % (diff)
        portfolio = ex45Portfolio.Portfolio()
        
        if diff <= 10:
            print PORTFOLIO_MIX['1']
            portfolio.allocate(PORTFOLIO_MIX['1'])
        elif 10 < diff and diff < 20:
            print PORTFOLIO_MIX['2']
            portfolio.allocate(PORTFOLIO_MIX['2'])
        else:
            print PORTFOLIO_MIX['3']
            portfolio.allocate(PORTFOLIO_MIX['3'])
        
#        print 'your portfolio mix is %d stocks and %d bonds' %(stocks, bonds)
    