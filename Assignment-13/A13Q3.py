# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A13Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-13\A13Q3.py
# Subject : 3. Write a program which accepts one number and checks whether it is perfect number or not.
# Description : Input: 6    Output: Perfect Number
# =============================================================================

def Divisors(Value):
    divs = []
    for i in range(1,Value):
        if Value%i==0:
            divs.append(i)
    return divs
            

def main():
    iValue = int(input("Enter The Number : "))
    DivisorsList = Divisors(iValue)
    print("Ours Divisors is : ",DivisorsList)

    DivAdd = sum(DivisorsList)
    if DivAdd == iValue:
        print(f"'{iValue} is the Perfect number")
    else:
        print(f"'{iValue} is not a Perfect number")

if __name__ == "__main__":
    main()
    