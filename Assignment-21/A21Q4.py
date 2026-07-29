# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A21Q4.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-21\A21Q4.py
# Subject/Question : Design a Python application that creates two threads.
# Description : 
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.
# =============================================================================

import threading
# ---------------------------------------------------------------------------
# Thread Class for Sum
# ---------------------------------------------------------------------------
class SumThread(threading.Thread):

    def __init__(self, Data):
        super().__init__()
        self.Data = Data
        self.Result = 0

    def run(self):

        Total = 0

        for Value in self.Data:
            Total += Value

        self.Result = Total


# ---------------------------------------------------------------------------
# Thread Class for Product
# ---------------------------------------------------------------------------
class ProductThread(threading.Thread):

    def __init__(self, Data):
        super().__init__()
        self.Data = Data
        self.Result = 1

    def run(self):

        Product = 1

        for Value in self.Data:
            Product *= Value

        self.Result = Product


# ---------------------------------------------------------------------------
# Main Function
# ---------------------------------------------------------------------------
def main():

    Data = [1, 2, 3, 4, 5]

    print("Input List :", Data)

    T1 = SumThread(Data)
    T2 = ProductThread(Data)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("\nSum     :", T1.Result)
    print("Product :", T2.Result)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()