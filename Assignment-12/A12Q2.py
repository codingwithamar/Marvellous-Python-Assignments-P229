# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A12Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-12\A12Q2.py
# Subject : 2. Write a program which accepts one number and prints its factors.
# Description : Input: 12 Output: 1 2 3 4 6 12
# =============================================================================

def factors(Value):
    RetArray = []
    for i in range(1,Value+1):
        if Value % i == 0:
            RetArray.append(i)
            i += 1
    return RetArray

def main():
    print("Enter the One Number")
    Num = int(input())

    Ret = factors(Num)
    print(f"'{Ret}' is the factors of '{Num}'")

if __name__ == "__main__":
    main()
    