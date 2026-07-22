# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A18Q3.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-18\A18Q3.py
# Subject : 3.Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List.
# Description : # Input Elements : 13 5 45 7
#                   Output : 5
# =============================================================================

def main():
    Values = []
    while True:
        Data = input("Enter the Data :")

        if Data == "":
            break

        Values.append(int(Data))
        
    Lowest = min(Values)
    print("Your Lowest Value is : ",Lowest)


if __name__ == "__main__":
    main()
    