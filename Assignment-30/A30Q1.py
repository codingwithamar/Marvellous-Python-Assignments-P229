# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A30Q1.py
# Path    : Assignment-30/A30Q1.py
# Subject : Write a Python program that prints:
# Jay Ganesh...     every two seconds.
# Description : Use:  schedule.every(2).seconds.do(...)
# Expected output:  Jay Ganesh...Jay Ganesh...Jay Ganesh...
# =============================================================================

import schedule
import time
import datetime

def Display():
    print("jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script Started")

    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()