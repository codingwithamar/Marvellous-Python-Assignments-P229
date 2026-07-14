# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A11Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-11\A11Q5.py
# Subject : 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Description : Input: 121  Output: Palindrome
# =============================================================================

def main():
    print("Enter the number")
    number = input()
    reverse = number[::-1]
    if number == reverse:
        print("Number is Palindrome")
    
    else:
        print("Number is not Palindrome")

if __name__ == "__main__":
    main()