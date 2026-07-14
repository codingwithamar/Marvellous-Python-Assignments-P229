# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A11Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-12\A11Q5.py
# Subject : 5. Write a program which accepts one number and prints that many numbers in reverse order.
# Description : Input: 5    Output: 5 4 3 2 1
# =============================================================================

def main():
    print("Enter One Number")
    Num = int(input())

    for i in range(Num,0,-1):
        print(i)    

if __name__ == "__main__":
    main()