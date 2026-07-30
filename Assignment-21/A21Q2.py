# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A21Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-21\A21Q2.py
# Subject/Question : 2: Design a Python application that creates two threads.
# Description : 
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.
# =============================================================================

import threading
import queue

def Max(iValues,iTQ1):
    MaxNumber = max(iValues)
    iTQ1.put(MaxNumber)

def Min(iValues,iTQ2):
    MinNumber = min(iValues)
    iTQ2.put(MinNumber)

def main():
    print("Enter the list of Numbers")
    Values = list(map(int,input().split()))
    print("You entered list is  : ",Values)

    TQ1 = queue.Queue()
    TQ2 = queue.Queue()

    T1 = threading.Thread(target=Max, name="Maximum", args = (Values,TQ1))
    T2 = threading.Thread(target=Min, name="Minimum", args = (Values,TQ2))

    T1.start()
    T2.start()
    T1.join()
    T2.join()

    MaxNumber = TQ1.get()
    MinNumber = TQ2.get()

    print("Maximum number of the list is : ",MaxNumber)
    print("Minimun number of the list is : ",MinNumber)

if __name__ == "__main__":
    main()
    