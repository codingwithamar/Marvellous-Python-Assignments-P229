# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A18Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-18\A18Q4.py
# Subject : 4.Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.
# Description :
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
# Element to search : 5     Output : 3

# =============================================================================

def Count(iValues,iSearchingNumber):
    Cnt = 0
    for i in iValues:
        if i == iSearchingNumber:
            Cnt = Cnt + 1
    return Cnt

def main():
    print("Enter the Values : ")
    Values = list(map(str,input().split()))

    print("Enter the Searching Number : ")
    SearchingNumber = str(input())

    print("Your Number List is : :",Values)
    print("Your Searching Number is : ",SearchingNumber)

    NumberCount = Count(Values,SearchingNumber)
    print("Your SearchingNumber Count in List is : ",NumberCount)

if __name__ == "__main__":
    main()