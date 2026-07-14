# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A12Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-12\A12Q1.py
# Subject : 1. Write a program which accepts one character and checks whether it is vowel or consonant.
# Description : Input: a  Output: Vowel
# =============================================================================

def CheckWhether(Text):
    Vowels = "aeiouAEIOU"
    if Text in Vowels:
        print(f"'{Text}' is Vowels")
    
    else:
        print(f"'{Text}' is Consonant")

def main():
    print("Enter the Word")
    Word = input()

    CheckWhether(Word)

if __name__ == "__main__":
    main()