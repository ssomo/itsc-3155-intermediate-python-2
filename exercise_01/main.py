#import the BankAccount class from the BankAccount file
from BankAccount import BankAccount
#Main method
if __name__ == '__main__':
    #Creates an instance of the BankAccount class
    acc = BankAccount('Sam', 1500)
    #Calls the deposit function
    acc.deposit(500)
    #Calls the withdraw function
    acc.withdraw(300)
    #Calls the get_balance() function
    print(acc.get_balance())