# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A20Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-20\A20Q4.py
# Subject/Question : 
# 4: Design a Python application that creates three threads named Small, Capital, and Digits. 
# Description : 
# • All threads should accept a string as input. 
# • The Small thread should count  display the number of lowercase characters.
# • The Capital thread should count & display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits. 
# • Each thread must also display: ◦ Thread ID ◦ Thread Name
# =============================================================================

import threading
import queue

def Small(iStrings,iQT1):
    print()
    print("-"*15,"Small Thread Started","-"*15)

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Charlist = []
    for char in iStrings:
        if char.islower():
            Charlist.append(char)
    iQT1.put(Charlist)
    print("-"*15,"Small Thread Ended","-"*15)
    print()

def Capital(iStrings,iQT2):
    print()
    print("-"*15,"Capital Thread Started","-"*15)

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Charlist = []
    for char in iStrings:
        if char.isupper():
                Charlist.append(char)
    iQT2.put(Charlist)
    print("-"*15,"Capital Thread Ended","-"*15,)
    print()

def Digit(iStrings,iQT3):
    print()
    print("-"*15,"Digit Thread Started","-"*15)

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Charlist = []
    for char in iStrings:
        if char.isdigit():
            Charlist.append(char)
    iQT3.put(Charlist)
    print("-"*15,"Digit Thread Ended","-"*15)
    print()

def Spaces(iStrings,iQT4):
    print()
    print("-"*15,"Space Thread Started","-"*15)

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Charlist = []
    for char in iStrings:
        if char.isspace():
            Charlist.append(char)
    iQT4.put(Charlist)    
    print("-"*15,"Space Thread Ended","-"*15)
    print()

def main():
    print("*"*20,"MAIN PROCESS STARTED","*"*20)
    Strings = input("Enter the Lines : ")
    print("You Entered Lines is :\n",Strings)

    QT1 = queue.Queue()
    QT2 = queue.Queue()
    QT3 = queue.Queue()
    QT4 = queue.Queue()

    T1 = threading.Thread(target = Small, name = "Small", args = (Strings,QT1))
    T2 = threading.Thread(target = Capital, name = "Capital", args = (Strings,QT2))
    T3 = threading.Thread(target = Digit, name = "Digit", args = (Strings,QT3))
    T4 = threading.Thread(target = Spaces, name = "Space", args = (Strings,QT4))

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    T3.start()
    T3.join()

    T4.start()
    T4.join()

    Rsmall = QT1.get()
    RCapital = QT2.get()
    RDigit = QT3.get()
    RSpace = QT4.get()

    print()
    print("*"*20,"COUNTS","*"*20)
    print("Small letters count from your lines : ",len(Rsmall))
    print("Capital letters count from your lines : ",len(RCapital))
    print("Digits Count from your lines : ", len(RDigit))
    print("Spaces Count from your lines : ",len(RSpace))

    print()
    print("*"*20,"DISPLAY","*"*20)
    print("Small Letters : ", Rsmall)
    print("Capital Letters : ", RCapital)
    print("Digits : ", RDigit)
    print("Spaces : ", RSpace)

    print()
    print("*"*20,"MAIN PROCESS ENDED","*"*20)

if __name__ == "__main__":
    main()