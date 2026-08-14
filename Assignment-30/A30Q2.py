# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A30Q2.py
# Path    : Assignment-30/A30Q2.py
# Subject : Write a Python program that displays the current date and time after every one minute.
# Description : Use the datetime module.
# Expected output: Current Date and Time: 25-07-2026 04:30:00 PM
# =============================================================================

import schedule
import time
import datetime

def Display():
    print("Current Date and Time : ",datetime.datetime.now())

def main():
    print("Automate Script Started")

    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()