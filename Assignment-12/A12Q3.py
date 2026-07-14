# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A12Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-12\A12Q3.py
# Subject : 3. Write a program which accepts two numbers and 
# prints addition, subtraction,multiplication and division.
# Description : + - * /
# =============================================================================

def Add(No1,No2):
    return No1 + No2

def Sub(No1,No2):
    return No1 - No2

def Multi(No1,No2):
    return No1 * No2

def Div(No1,No2):
    return No1 / No2

def main():
    print("Enter Value1")
    Value1 = int(input())

    print("Enter Value2")
    Value2 = int(input())

    Addition = Add(Value1, Value2)
    print(f"'{Value1}' and '{Value2}' Addition is :", Addition)

    Substraction = Sub(Value1, Value2)
    print(f"'{Value1}' and '{Value2}' Substraction is :", Substraction)
    
    Multiplication = Multi(Value1, Value2)
    print(f"'{Value1}' and '{Value2}' Multiplication is :",Multiplication)

    Division = Div(Value1, Value2)
    print(f"'{Value1}' and '{Value2}' Division is :", Division)

    print("-------Thank You---------")
    
if __name__ == "__main__":
    main()
    
    