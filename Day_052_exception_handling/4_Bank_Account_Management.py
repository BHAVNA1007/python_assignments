'''
4_Bank_Account_Management
Objective: Create a program to manage bank accounts and handle exceptions for insufficient balance and negative deposit amounts.

Details:
Create a BankAccount class with fields for accountNumber, accountHolder, and balance.
Define two custom exceptions:
InsufficientBalanceException for withdrawal amounts exceeding the balance.
NegativeDepositException for deposits with negative amounts.
Include methods for deposit(double amount) and withdraw(double amount) that throw the respective exceptions.
In the main method, demonstrate various cases like successful transactions, insufficient balance, and invalid deposits.
'''

class InsufficientBalanceException(Exception):
   pass

class NegativeDepositException(Exception):
   pass

class BankAccount:
 
  def __init__(self, accountNumber, accountHolder, balance):
     self.accountNumber = accountNumber
     self.accountHolder = accountHolder
     self.balance = balance

  def deposits(self, amount):
  
      if amount < 0:
         raise NegativeDepositException("amount should not be negative")

      self.balance = self.balance + amount
      print("deposite successfully")
      print("current balance: ", self.balance) 

  def withdraw(self, amount):
     
      if amount > self.balance:
         raise InsufficientBalanceException("insufficient balance")
      
      self.balance = self.balance - amount

      print("successfully withdraw")
      print("current balance: ", self.balance)

accno = int(input("Account number: "))
acholder = input("account Holder: ")
balance = int(input("Balance "))

acc = BankAccount(accno, acholder, balance)

try:
    amount = int(input("Amount: "))
    acc.deposits(amount)

except NegativeDepositException as e:
    print("NegativeDepositException", e)

try:
    amount = float(input("Amount: "))
    acc.withdraw(amount)

except InsufficientBalanceException as e:
    print("InsufficientBalanceException", e)
          
       
