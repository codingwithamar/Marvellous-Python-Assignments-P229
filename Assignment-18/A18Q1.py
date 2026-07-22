# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A18Q1.py
# Path    : Assignment-18/A18Q1.py
# Subject : 1.Write a program which accept N numbers from user and store it into List. 
# Return addition of all elements from that List.
# Description : Description
# =============================================================================

from functools import reduce

def Add(iValue1,iValue2):
    return iValue1+iValue2

def main():
    Values = []
    while True:
        Data = input("Enter the Values : ")

        if Data == "":
            break

        Values.append(int(Data))
        
    Addition = reduce(Add,Values)
    print("Addition of All Numbers : ",Addition)


if __name__ == "__main__":
    main()
    