# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A11Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-11\A11Q4.py
# Subject : 4. Write a program which accepts one number and prints reverse of that number.
# Description : Input: 123  Output: 321
# =============================================================================

def main():
    print("Enter the Number")
    digit = input()
    print("Reverse Digit is : ", digit[::-1])

if __name__ == "__main__":
    main()