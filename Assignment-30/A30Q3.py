# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A30Q3.py
# Path    : Marvellous-Python-Assignments-P229/Assignment-30/A30Q3.py
# Subject : 3: Write a program that schedules a function to print:
# Description : Coding Kar..!
# every 30 minutes.
# =============================================================================

import schedule
import time
import datetime

def Display():
    print("Coding Kar...")

def main():
    print("Automate Script Started")

    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
