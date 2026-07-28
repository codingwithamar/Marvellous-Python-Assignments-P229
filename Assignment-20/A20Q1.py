# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A20Q1.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-20\A20Q1.py
# Subject : 1: Design a Python application that creates two separate threads named Even and Odd
# Description : 
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module
# • Ensure proper thread creation and execution
# =============================================================================

import threading

def Even():
    print("T1 - Even Thread Started")
    for i in range(2,21,2):
        print(i)
    print("T1 - Even Thread Ended")

def Odd():
    print("T2 - Odd Thread Started")
    for i in range(1,21,2):
        print(i)
    print("T2 - Odd Thread Ended")

def main():
    print("Main Threading Started")
    T1 = threading.Thread(target=Even,name="Even")    #thread 1 Created
    T2 = threading.Thread(target=Odd,name="Odd")      #thread 2 Created

    T1.start()      #Starting Thread 1
    T1.join()       

    T2.start()      #Starting Thread 2
    T2.join()

    print("Main Thread Ended")

if __name__ == "__main__":
    main()
    