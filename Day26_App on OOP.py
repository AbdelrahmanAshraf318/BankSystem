# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:33:12 2020

@author: Abd Elrahman
"""


from numpy import *

class User:
    def __init__(self):
        self.__Name = "Nothing"
        self.__Balance = 0
        self.__AccountNumber = 0
    
    def SetName(self , Name):
        self.__Name = Name
    
    def GetName(self):
        return self.__Name
    
    def SetBalance(self , Balance):
        self.__Balance = Balance
    
    def GetBalance(self):
        return self.__Balance
    
    def SetAccountNumber(self):
        self.__AccountNumber = random.randint(10000 , 99999)
    
    def GetAccountNumber(self):
        return self.__AccountNumber
    
    

################################################################
        
class SavingAccounts:
     __Users = {}
     __user = User()
     def SetUser(self , obj):
          self.__Users[obj.GetAccountNumber()] = [obj.GetBalance() , obj.GetName()]
         
     def Check(self , Name , AccountNumber):
         if AccountNumber in self.__Users.keys():
             if self.__Users[AccountNumber][1]==Name:
                 return True
         return False
     def Deposit(self , Money , AccountNumber):
         if AccountNumber in self.__Users.keys():
             self.__Users[AccountNumber][0] +=  Money
         else:
             print("There is no accountNumber like that")
     def Withdraw(self , Money , AccountNumber):
         if AccountNumber in self.__Users.keys():
             if self.__Users[AccountNumber][0]>=Money:
                 self.__Users[AccountNumber][0] -=  Money
             else:
                print("There is no enough balance")
         else:
             print("There is no accountNumber like that")
    
     def Display(self):
         print(self.__Users)
     
        
        
user = User()
account = SavingAccounts()

while True:
    print("Enter 1 to Sign up")
    print("Enter 2 to log in")
    print("Enter 3 to display Accounts")
    print("Enter 4 to Exit")
    choice = int(input("Enter your choice: "))
    if choice is 1:
        Name = str(input("Enter your Name: "))
        user.SetName(Name)
        Balance = int(input("Enter Balance: "))
        user.SetBalance(Balance)
        user.SetAccountNumber()
        print("Your AccountNumber is: " , user.GetAccountNumber())
        account.SetUser(user)
    elif choice is 2:
         Name = str(input("Enter your Name: "))
         user.SetName(Name)
         AccountNumber = int(input("Enter your AccountNumber: "))
         passed = account.Check(Name , AccountNumber)
         if passed==True:
             while True:
                 print("Enter 1 to Withdraw")
                 print("Enter 2 to Deposit")
                 print("Enter 3 to return to big menu")
                 choose = int(input("Enter your choice: "))
                 if choose is 1:
                     Money = int(input("Enter the money you want to withdraw: "))
                     account.Widhraw(AccountNumber , Money)
                 elif choose is 2:
                     Money = int(input("Enter the money you want to withdraw: "))
                     account.Deposit(Money , AccountNumber)
                 elif choose is 3:
                     break
    elif choice is 3:
        account.Display()
    elif choice is 4:
        print("Thanks for using my program")
        break
        
















    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    