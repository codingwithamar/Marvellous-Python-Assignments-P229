# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A14Q10.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-14\A14Q10.py
# Subject : 10. Write a lambda function which accepts three numbers and returns largest number.
# Description : Input 3 Numbers and Output Largest Number
# =============================================================================

BigValue = lambda liValue1, liValue2, liValue3 : (
    liValue1 if liValue1 > liValue2 and liValue1 > liValue3
    else liValue2 if liValue2 > liValue1 and liValue2 > liValue3
    else liValue3)

def main():     
    iValue1 = int(input("Enter the Value 1 : "))
    iValue2 = int(input("Enter the Value 2 : "))
    iValue3 = int(input("Enter the Value 3 : "))

    Ret = BigValue(iValue1, iValue2, iValue3)
    print("Big Value is : ",Ret)

if __name__ == "__main__":
    main()
    
