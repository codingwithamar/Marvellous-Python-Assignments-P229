# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A20Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-20\A20Q2.py
# Subject : 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# Description : 
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
#   ◦ Identify all even factors of the given number.
#   ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
#   ◦ Identify all odd factors of the given number.
#   ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message: “Exit from main”
# =============================================================================

import threading

#----------------------------------Thread Definations----------------------------------------
def EvenFactor(iValues):
    print("\n---------Even Thread Start---------")
    EvenNumbers = []
    for iValue in iValues:
        if iValue%2==0:
            EvenNumbers.append(iValue)
    print("Even Numbers : ",EvenNumbers)
    print("Total Even Number count from your list is : ",len(EvenNumbers))
    print("Addition of Even Numbers : ", sum(EvenNumbers))
    print("---------Even Thread Ended---------\n")

def OddFactor(iValues):
    print("\n---------Odd Thread Start---------")
    OddNumbers = []
    for iValue in iValues:
            if iValue%2!=0:
                OddNumbers.append(iValue)
    print("Odd Numbers : ",OddNumbers)
    print("Total Odd Number count drom your list is : ",len(OddNumbers))
    print("Addition of Odd Numbers : ", sum(OddNumbers))
    print("---------Even Thread Ended---------\n")

def main():
    print("************{Start Main Function}**************\n")
    Values = []
    print("Enter the Number : ")
    Values = list(map(int,input().split()))
    print("You Entered list of Numbers is : ",Values)

#----------------------------------Thread Creations----------------------------------------
    T1 = threading.Thread(target=EvenFactor, name="EvenFactor", args=(Values,))
    T2 = threading.Thread(target=OddFactor, name="OddFactor", args=(Values,))

#----------------------------------Thread Operations----------------------------------------
    T1.start()  #Thread1 Started
    T2.start()  #Thread2 Started
    T1.join()   #Thread1 Wait for Another Thread
    T2.join()   #Thread2 Wait for Another Thread

    #ithe at a time donhi thread run kelet tyamule output mix format madhe yeil

    print("************{End Main Function}**************")

if __name__ == "__main__":
    main()
    