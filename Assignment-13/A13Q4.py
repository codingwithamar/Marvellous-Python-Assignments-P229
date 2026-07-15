# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A13Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-13\A13Q4.py
# Subject : 4. Write a program which accepts one number and prints binary equivalent.
# Description :          
#          13 ÷ 2 = 6  Remainder = 1
#          6 ÷ 2 = 3  Remainder = 0
#          3 ÷ 2 = 1  Remainder = 1
#          1 ÷ 2 = 0  Remainder = 1
# =============================================================================

def DTOB(Value):
    Remainder = []
    while Value > 0:
        remain = Value % 2
        Remainder.append(remain)
        Value = Value // 2 
        rem = Remainder[::-1]
    return rem

def main():

    Decimal = int(input("Enter the Decimal Number : "))
    BinaryList = DTOB(Decimal)
    print(BinaryList)


if __name__ == "__main__":
    main()
    