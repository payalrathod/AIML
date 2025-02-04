# from random import randint
#
#
# class Bank:
#     pass
#
#
# class NewSavingAccount(Bank):
#     newName = input()
#     initial_deposit = input()
#     newAccountNumber = randint(10000, 99999)  # randint is inclusive at both ends
#
# class ExistingAccount(Bank):
#     oldName = input()
#     oldAccountNumber = input()
#
#     def Withdraw(self):
#         pass
#     def Deposit(self):
#         pass
#     def DisplayBalance(self):
#         pass
#
# user = Bank()  # objects
# new_user = NewSavingAccount()
# old_user = ExistingAccount()
#
# while True:
#     user = int(input())
#     if user is 1:
#         user.Bank()
#     elif user is 2:
#         req = new_user.NewSavingAccount()
#         user.BorrowBooks(req)
#     elif user is 3:
#         ret = old_user.returnBook()
#         user.UpdateBooksAfterReturn(ret)
#     elif user is 4:
#         quit()
from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self, name, initalDeposit):
        return 0
    @abstractmethod
    def authentication(self,name,accountNumber):
        return 0
    @abstractmethod
    def withdraw(self,withdrawalAmount):
        return 0
    @abstractmethod
    def deposit(self, depositAmount):
        return 0

class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts = {}
    #     [key][0] => name ; [key][1] => balance
    def createAccount(self, name, initalDeposit):
        self.accountnumber = randint(10000,99999)
        self.savingAccounts[self.accountnumber] = [name, initalDeposit]
        print("New Account ", self.accountnumber)
    def authentication(self,name,accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountnumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self,withdrawalAmount):
        if withdrawalAmount > self.savingAccounts[self.accountnumber][1]:
            print("Invalid Amount")
        else:
            self.savingAccounts[self.accountnumber][1] -= withdrawalAmount
            # print("Balance after withdrawal ", self.savingAccounts[self.accountnumber][1])
            print("Balance after withdrawal")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingAccounts[self.accountnumber][1] += depositAmount
        # print("Balance after deposit ", self.savingAccounts[self.accountnumber][1])
        print("Balance after deposit")
        self.displayBalance()

    def displayBalance(self):
        print("Balance ",self.savingAccounts[self.accountnumber][1])

savingAcount = SavingAccount()
while True:
    print("Enter 1 new count")
    print("Enter 2 to old account")
    print("Ener 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter Name ")
        name = input()
        print("initial Deposit")
        deposit = int(input())
        savingAcount.createAccount(name,deposit)
    if userChoice is 2:
        print("Enter name")
        name = input()
        print("Enter Account number")
        accountnumber = int(input())
        authenticat = savingAcount.authentication(name,accountnumber)
        if authenticat is True:
            while True:
                print("enter 1 to withdraw")
                print("enter 2 to deposit")
                print("enter 3 to display available balance")
                print("enter 4 to previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print("enter withdraw amount")
                    withDraw =  int(input())
                    savingAcount.withdrawalAmount(withDraw)
                elif userChoice is 2:
                    print("Enter amount to deposit")
                    depositAmount = int(input())
                    savingAcount.deposit(depositAmount)
                elif userChoice is 3:
                    savingAcount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()




