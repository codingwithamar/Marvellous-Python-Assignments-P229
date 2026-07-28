# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A20Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-20\A20Q5.py
# Subject/Question : 
# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# Description : 
# • Thread1 should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.
# • Ensure that:
#       ◦ Thread2 starts execution only after Thread1 has completed.
# • Use appropriate thread synchronization
# =============================================================================

import threading

EventObj = threading.Event()

def Thread1():
    for i in range(1,51,1):
        print(i)
    EventObj.set()  #Signal passed when completed

def Thread2():
    EventObj.wait() #wait for Thread1 ending
    for i in range(50,0,-1):
        print(i)

def main():
    T1 = threading.Thread(target = Thread1, name ="Thread1") 
    T2 = threading.Thread(target = Thread2, name ="Thread2")

    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__ == "__main__":
    main()