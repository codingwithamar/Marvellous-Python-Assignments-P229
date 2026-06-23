#Author : codingwithamar@gmail.com
#Description : 'A3Q1 : Write a function to accept two numbers and return their multiplication'

def Multiplication(No1, No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

def main():
    print("Enter First Number")
    Value1 = int(input())
    
    print("Enter Second Number")
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)

    print("Your Multiplication is :", Ret)

if __name__ == "__main__":
    main()