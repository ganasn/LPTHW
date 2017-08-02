#Exercise 45 - The Game
#Portfolio class
#Defines the stock/bond mix based on customer's risk profile identified

class Portfolio(object):
    
    stocks = 0
    bonds = 0
    
    def __init__(self):
#        print 'In ex45Portfolio.Portfolio.__init__()'
#        print portfolio_mix
#        exit(0)
        pass
    
    def conservative(self):
        stocks = 20
        bonds = 80
        return stocks, bonds
        
    def moderate(self):
        stocks = 50
        bonds = 50
        return stocks, bonds
        
    def aggressive(self):
        stocks = 80
        bonds = 20
#        print 'Your allocation is %d\% in stocks and %d\% in bonds' %(stocks, bonds)
        return stocks, bonds
    
    def allocate(self, allocation):
        print 'In ex45Portfolio.Portfolio.allocate() with parameter %s' % allocation
        if allocation == 'conservative':
            print 'inside conservative call'
            stocks = 20
#            bonds = 80
#Running into function call issues, so re-creating this allocation inside allocate() instead of passing to another function
#            conservative()
        elif allocation == 'moderate':
            print 'inside moderate call'
            stocks = 50
#            bonds = 100 - stocks
#            moderate()
        else:
            print 'inside aggressive call'
            stocks = 80
#            bonds = 100 - stocks
#            aggressive()
        bonds = 100 - stocks
        print 'Your allocation is %d percent in stocks and %d percent in bonds' %(stocks, bonds)
        
    
        
    