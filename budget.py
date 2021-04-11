
class Category:  
  
    def __init__(self, name, balance, minimumBalace=100):
        self.name = name
        self.balance = balance
        self.minimumBalace = minimumBalace
        
        
    def deposit(self, amount):
        self.balance += amount
        print("{} deposit was successful".format(amount))
        
    def withdraw(self, amount):
        if(self.balance - amount > self.minimumBalace):
          self.balance -= amount
          print("{} withdrawal was successful".format(amount))
        else:
          print("{} withdrawal failed!! The minimum balance must not be less than 500".format(amount))
    
    def transfer(self, amount, category):        
        if(self.balance - amount > self.minimumBalace):
          self.balance -= amount
          category.balance += amount
          print("{} transfer to {} was successful".format(amount, category.name))
        else:
          print("{} transfer to {} failed!!".format(amount, category.name))

    def get_balance(self):
        return self.balance           



           
food = Category("food", 100)
food.deposit(10000)
print(food.get_balance())  
food.withdraw(5000)
food.withdraw(30)
print(food.get_balance())    
entertainment = Category("entertainment", 800)
food.transfer(300, entertainment)
entertainment.withdraw(1150)
print(entertainment.get_balance())
