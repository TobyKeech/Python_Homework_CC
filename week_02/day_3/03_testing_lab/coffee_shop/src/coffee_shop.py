class CoffeeShop:
    
    def __init__(self,name,till,drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def drinks_list(self):
        return len(self.drinks)
    
    def add_cash_to_till(self,amount):
         self.till += amount
         
    def sell_drink(self,customer,drink):
        customer.reduce_cash(drink.price)
        self.add_cash_to_till(drink.price)

    def checks_age(self,customer):
        return customer.age >= 16
         
    def check_energy_level(self,customer):
        return customer.energy_level <= 50       
            


