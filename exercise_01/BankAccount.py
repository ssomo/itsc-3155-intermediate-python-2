#Create a Bank Account class
class BankAccount:
    #Constructor to initialize the instance fields
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        #Adds the deposit amount to the balance
        self.balance += amount

    def withdraw(self, amount):
        #Checks if the account has enough to withdraw the amount
        if self.balance < amount:
            #Displays this message
            print('Sorry, you have insufficient funds')
        else:
            #Subtracts the withdrawal amount from the account balance
            self.balance -= amount

    def get_balance(self):
        #Returns the account balance
        return str(self.account_name) + ' has a balance of $' + str(self.balance)
    