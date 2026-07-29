# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A21Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-21\A21Q1.py
# Subject/Question : 1: Design a Python application that creates two threads named Prime and NonPrime.
# Description : • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.
# =============================================================================

import threading
import queue

def Prime(iValues,iQT1):
    PrimeList = []
    for value in iValues:
        count = 0
        for i in range(1,value+1):
            if value%i==0:
                count = count + 1
        if count == 2:
            PrimeList.append(value)
    iQT1.put(PrimeList)

def NonPrime(iValues,iQT2):
    NonPrimeList = []
    for value in iValues:
        count = 0
        for i in range(1,value+1):
            if value%i==0:
                count = count + 1
        if count != 2:
            NonPrimeList.append(value)
    iQT2.put(NonPrimeList)

def main():
    print("Enter the list of numbers : ")
    Values = list(map(int,input().split()))
    print("Entered list is : ", Values)

    QT1 = queue.Queue()
    QT2 = queue.Queue()

    T1 = threading.Thread(target = Prime, name = "Prime", args = (Values,QT1))
    T2 = threading.Thread(target = NonPrime, name = "NonPrime", args = (Values,QT2))

    T1.start()
    T2.start()
    T1.join()
    T2.join()

    RPrime = QT1.get()
    RNonPrime = QT2.get()

    print("All Prime Numbers from list : ",RPrime)
    print("All NonPrime Numbers from list : ", RNonPrime)

if __name__ == "__main__":
    main()