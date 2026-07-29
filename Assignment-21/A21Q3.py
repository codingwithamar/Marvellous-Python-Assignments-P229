# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A21Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-21\A21Q3.py
# Subject/Question : 3: Design a Python application where multiple threads update a shared variable.
# Description : • Use a Lock to avoid race conditions. 
# • Each thread should increment the shared counter multiple times. 
# • Display the final value of the counter after all threads complete execution.
# =============================================================================

import threading

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter
    for i in range(100000):
        Lock.acquire()
        Counter += 1
        Lock.release()

def main():
    global Counter

    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)
    T3 = threading.Thread(target=Increment)

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final Counter :", Counter)

if __name__ == "__main__":
    main()


