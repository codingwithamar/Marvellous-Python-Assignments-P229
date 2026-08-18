# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A30Q6.py
# Path    : Marvellous-Python-Assignments-P229/Assignment-30/A30Q6.py
# Subject : 6: Write a script that schedules the following tasks:
# •Print Lunch Time! every day at 1:00 PM.
# •Print Wrap up work every day at 6:00 PM.
# Description :  Both tasks should be handled by separate functions.
# =============================================================================

import time
import schedule
import datetime

def LunchTime():
    print("Lunch Time !")
    print(datetime.datetime.now())

def WrapUpTime():
    print("Wrap Up")
    print(datetime.datetime.now())

def main():
    print("Automate script Started")

    schedule.every().day.at("13:00").do(LunchTime)

    schedule.every().day.at("06:00").do(WrapUpTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("Automate Script Ended")

if __name__ == "__main__":
    main()