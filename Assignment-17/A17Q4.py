# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q4.py
# Subject : 4.Write a program which accept one number form user and return addition of its factors.
# Description : Input : 12 Output : 16 (1+2+3+4+6)
# =============================================================================

def main():
    Add = 0
    print("Enter the Value :")
    Value = int(input())
    for i in range(1,Value,1):
        if Value%i==0:
            Add+=i
        else:
            i+1
    print("Addition of Factors is ", Add)

if __name__ == "__main__":
    main()