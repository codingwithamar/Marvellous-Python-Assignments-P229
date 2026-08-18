# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A30Q4.py
# Path    : Marvellous-Python-Assignments-P229/Assignment-30/A30Q4.py
# Subject : 4: Create a task that executes every day at 9:00 AM and prints:
# Namskar...
# Description : Use: schedule.every().day.at(“09:00").do(...)
# =============================================================================

import time
import schedule
import datetime

def Display():
    print("Namaskar")
    print(datetime.datetime.now())

def main():
    print("Automate Script Started")

    schedule.every().day.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()