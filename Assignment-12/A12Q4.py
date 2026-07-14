# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A12Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-12\A12Q4.py
# Subject : 4. Write a program which accepts one number and prints that many numbers starting from 1.
# Description : Input: 5    Output: 1 2 3 4 5
# =============================================================================

def main():
    print("Enter One Number")
    Num = int(input())

    for i in range(1,Num+1):
        print(i)    

if __name__ == "__main__":
    main()