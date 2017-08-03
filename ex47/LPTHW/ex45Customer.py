#Exercise 45 - The Game
#The Customer Class
#Class to hold profile of customer

import ex45RiskProfile

class Customer(object):
    
    current_age = 0
    retirement_age = 0
#    portfolio_balance = 0
    
    def main(self):
        inputs_acquired = False
        while not inputs_acquired:
            try:
                current_age = int(raw_input('What\'s your current age in years?>'))
                retirement_age = int(raw_input('At what age do you plan to retire?>'))
#                portfolio_balance = int(raw_input('How much have you already saved?>'))
                inputs_acquired = True
                risk_profile = ex45RiskProfile.RiskProfile()
                risk_profile.allocate(current_age, retirement_age) 
#                risk_profile.allocate(current_age, retirement_age,portfolio_balance) 
            except ValueError:
                print 'You\'re required to provide numbers and you seem to have provided something else'
                continue
        
    
    def __init__(self):
        current_age = 0
        retirement_age = 0
#        portfolio_balance = 0
#        risk_profile = ex45RiskProfile.RiskProfile()
#        Despite __init__ defined past main(), this call to main() bombs 
#        That's because __init__ is called first and given the interpretive nature of Python, it does not recognize main()
#        main()
        
    
            
        
customer = Customer()
customer.main()