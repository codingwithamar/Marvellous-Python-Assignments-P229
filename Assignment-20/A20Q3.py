# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A20Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-20\A20Q3.py
# Subject/Question : 3: Design a Python application that creates two threads named EvenList and OddList.
# Description : 
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
#   ◦ Extract all even elements from the list.
#   ◦ Calculate and display their sum.
# • The OddList thread should:
#   ◦ Extract all odd elements from the list.
#   ◦ Calculate and display their sum.
# • Threads should run concurrently.
# =============================================================================

import threading
import queue

#----------------------------------Thread Definations----------------------------------------
def EvenFactor(iValues,QT1):
    print("\n---------Even Thread Start---------")
    EvenNumbers = []
    for iValue in iValues:
        if iValue%2==0:
            EvenNumbers.append(iValue)
    QT1.put(EvenNumbers)
    print("\n---------Even Thread Ended---------\n")

def OddFactor(iValues,QT2):
    print("\n---------Odd Thread Start---------\n")
    OddNumbers = []
    for iValue in iValues:
            if iValue%2!=0:
                OddNumbers.append(iValue)
    QT2.put(OddNumbers)    
    print("---------Odd Thread Ended---------\n")

def main():
    print("************{Start Main Function}**************\n")
    Values = []
    print("Enter the Number : ")
    Values = list(map(int,input().split()))
    print("You Entered list of Numbers is : ",Values)

#----------------------------------Thread Creations----------------------------------------
    QT1 = queue.Queue()
    QT2 = queue.Queue()
    T1 = threading.Thread(target=EvenFactor, name="EvenFactor", args=(Values,QT1))
    T2 = threading.Thread(target=OddFactor, name="OddFactor", args=(Values,QT2))

#----------------------------------Thread Operations----------------------------------------
    T1.start()  #Thread1 Started
    T2.start()  #Thread2 Started
    T1.join()   #Thread1 Wait for Another Thread
    T2.join()   #Thread2 Wait for Another Thread

#----------------------------------After Thread end Return Operations----------------------------------------
    REvenNumbers = QT1.get()
    ROddNumbers = QT2.get()

    print("\n\n----------{Even Results}----------")
    print("Even Numbers : ",REvenNumbers)
    print("Total Even Number count from your list is : ",len(REvenNumbers))
    print("Addition of Even Numbers : ", sum(REvenNumbers))

    print("\n\n----------{Odd Results}----------")
    print("Odd Numbers : ",ROddNumbers)
    print("Total Odd Number count drom your list is : ",len(ROddNumbers))
    print("Addition of Odd Numbers : ", sum(ROddNumbers))

    print("\n************{End Main Function}**************")


if __name__ == "__main__":
    main()
    