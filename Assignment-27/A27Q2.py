# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A27Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-27\A27Q2.py
# Subject/Question : Write a Python program to implement a class named BankAccount 
# with the following requirements:
# Description : 
# • The class should contain two instance variables: 
#       ◦ Name (Account holder name)
#       ◦ Amount (Account balance)
# • The class should contain one class variable:
#       ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
#       ◦ Display() – displays account holder name and current balance
#       ◦ Deposit() – accepts an amount from the user and adds it to balance
#       ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
#                   (Ensure withdrawal is allowed only if sufficient balance exists)
#       ◦ CalculateInterest() – calculates and returns interest using formula:
#                               Interest = (Amount * ROI) / 100
#  • Create multiple objects and demonstrate all methods.
# =============================================================================
class BankAccount:
    ROI = 10.5
    def __init__(self,Account_holder_name,Account_balance):
        self.Account_holder_name = Account_holder_name
        self.Account_balance = Account_balance

    def Display(self):
        print(
            f"Account Holder Name : {self.Account_holder_name}\n"
            f"Current Balance : {self.Account_balance}"
            )

    def Deposit(self):
        DepositAmount = int(input("Enter Deposit Amount : "))
        self.Account_balance += DepositAmount
        print("After Deposit letest Balance is : ",self.Account_balance)

    def Withdraw(self):
        self.WithdrawAmount = int(input("Enter the Withdraw Amount : "))
        if self.WithdrawAmount <= self.Account_balance:
            self.Account_balance = self.Account_balance - self.WithdrawAmount
            print("After Withdraw Account balance is : ",self.Account_balance)
        else:
            print("Insufficient Balance in Your Account")

    def CalculateInterest(self):
        self.Interest = (self.Account_balance * self.ROI)/100
        print("Your Saving Account Intrest is : ",self.Interest)
        self.NetBalance = self.Account_balance + self.Interest
        print("Net Balance : ",self.NetBalance)

def main():
    Obj1 = BankAccount("Amar Bhandare",100000)

    print("Please Select Operations :")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Calculate Interest")
    print("4. Display")
    print()
    Choice = int(input("Enter your choice : "))

    if Choice == 1:
        Obj1.Deposit()

    elif Choice == 2:
        Obj1.Withdraw()

    elif Choice == 3:
        Obj1.CalculateInterest()

    elif Choice == 4:
        Obj1.Display()

    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
