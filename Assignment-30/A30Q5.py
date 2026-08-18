# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A30Q5.py
# Path    : Marvellous-Python-Assignments-P229/Assignment-30/A30Q5.py
# Subject : Schedule a task that executes every five minutes.
# The task should write the current date and time into a file named:  Marvellous.txt
# New entries should be appended without removing previous entries.
# Description : Example file contents:
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM
# Task executed at: 25-07-2026 04:40:00 PM
# =============================================================================

import time
import schedule
import datetime

def WriteInsideFile():
    try:
        fobj = open("Marvellous.txt","a")
        print("File gets Opened")
        print("Processing..")
        NowTime = datetime.datetime.now()
        fobj.write(
            "Task Executed at : "
            +NowTime.strftime("%d-%m-%y %I-%M-%S-%p")
            +"\n")
        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current directory.")

def main():
    print("Automate script started")

    schedule.every(30).seconds.do(WriteInsideFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()