# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A11Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-11\A11Q3.py
# Subject : 3. Write a program which accepts one number and prints sum of digits.
# Description : Input: 123   Output: 6
# =============================================================================

def add(value):
    total = 0
    while value > 0:
        total += value % 10 #remainder dete
        value //= 10        #last digit remove karte
    return total    

        
    print("Addition of Digit is : ", i)

def main():
    print("Enter the Number")
    digit = int(input())
    Sum = add(digit)
    print("Sum of digit is : ", Sum)

if __name__ == "__main__":
    main()