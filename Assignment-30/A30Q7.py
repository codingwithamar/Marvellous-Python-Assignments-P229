# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A130Q7.py
# Path    : Marvellous-Python-Assignments-P229/Assignment-30/A130Q7.py
# Subject : Write a Python program that performs a file backup every hour.
# Description : The program should:
# 1.Accept the source file path.
# 2.Accept the destination directory path.
# 3.Copy the source file to the destination directory.
# 4.Add the current date and time to the backup filename.
# 5.Write the backup operation details into:  backup_log.txt
#   Example backup filename:    Data_25_07_2026_16_30_00.txt
# Example log entry:
# Backup completed successfully at 25-07-2026 04:30:00 PM
# Use the shutil module for file copying.

# =============================================================================

import shutil
import schedule
import time
from datetime import datetime
import os


def Backup(Source, Destination):

    CurrentTime = datetime.now()

    DateTime = CurrentTime.strftime("%d_%m_%Y_%H_%M_%S")

    FileName = os.path.basename(Source)

    Name, Extension = os.path.splitext(FileName)

    BackupFileName = Name + "_" + DateTime + Extension

    DestinationPath = os.path.join(Destination, BackupFileName)

    shutil.copy2(Source, DestinationPath)

    LogTime = CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p")

    LogFile = os.path.join(Destination, "backup_log.txt")

    with open(LogFile, "a") as File:
        File.write(
            "Backup completed successfully at "
            + LogTime
            + "\n"
        )

    print("Backup completed successfully at", LogTime)


def main():

    Source = input("Enter source file path : ")
    Destination = input("Enter destination directory path : ")

    schedule.every(1).minutes.do(Backup, Source, Destination)

    print("Backup scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()