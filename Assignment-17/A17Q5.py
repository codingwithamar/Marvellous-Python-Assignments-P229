# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q5.py
# Subject : 5.Write a program which accept one number for user and check whether number is prime or not.
# Description : Input : 5   Output : It is Prime Number
# =============================================================================

def main():
    Add = 0
    print("Enter the number : ")
    Value = int(input())

    for i in range(1,Value+1,1):
        if Value%i==0:
            Add += i
        else:
            i+1
    
    if Add == Value+1:
        print("This is Prime Number")
    else:
        print("This is not a prime Number")

if __name__ == "__main__":
    main()
    