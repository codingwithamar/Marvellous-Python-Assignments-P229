#Author : codingwithamar@gmail.com
"""Description : Write a program which accepts one number and checks whether it is divisible by 3 and 5
Input: 15
Output: Divisible by 3 and 5
"""

def divisible():
    print("Enter The value : ")
    value = int(input())

    if value%3==0 & value%5==0:
        print("Value is divisible")
    
    else:
        remain3 = value%3
        remain5 = value%5
        print("value is not divisible\n")
        print("3 by remaining is :", remain3)
        print("5 by remaining is :", remain5)

def main():
    divisible()
    
if __name__ == "__main__":
    main()
    