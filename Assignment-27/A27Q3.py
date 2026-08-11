# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A27Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-27\A27Q3.py
# Subject/Question : Write a Python program to implement a class named Numbers 
# with the following specifications: 
# Description : 
# • The class should contain one instance variable:
#        ◦ Value 
# • Define a constructor (__init__) that accepts a number from the user and initializes Value. 
# • Implement the following instance methods: 
#       ◦ ChkPrime() – returns True if the number is prime, otherwise returns False 
#       ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False 
#       ◦ Factors() – displays all factors of the number 
#       ◦ SumFactors() – returns the sum of all factors 
# • Create multiple objects and call all methods.
# =============================================================================

class Numbers():
    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            print('Not Prime')
            return False
        else:
            for i in range(2,int(self.Value ** 0.5)+1):
                if self.Value % i == 0:
                    print("Not Prime")
                    return False
            else:
                print(f"{self.Value} is Prime Value")
                return True

    def ChkPerfect(self):
        FactAdd = 0
        for i in range(1,self.Value,1):
            if self.Value % i == 0:
                FactAdd = FactAdd + i
        if FactAdd == self.Value:
                print(f"{self.Value} is Perfect Value")
        else:
                print("Not Perfect")
        return FactAdd == self.Value

    def Factors(self):
        Factorslist = []
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                Factorslist.append(i)
        print("Factor are : ",Factorslist)

    def SumFactors(self):
        Factorslist = []
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                Factorslist.append(i)
        print("SumFactor is : ",sum(Factorslist))
        return sum(Factorslist)


def main():
    Value = int(input("Enter the Value : "))
    Obj1 = Numbers(Value)
    Obj1.ChkPrime()
    Obj1.ChkPerfect()
    Obj1.Factors()
    Obj1.SumFactors()

    Value = int(input("Enter the Value : "))
    Obj2 = Numbers(Value)
    Obj2.ChkPrime()
    Obj2.ChkPerfect()
    Obj2.Factors()
    Obj2.SumFactors()


if __name__ == "__main__":
    main()