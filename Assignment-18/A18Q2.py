# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A18Q2.py
# Path    : Assignment-18/A18Q2.py
# Subject : 2.Write a program which accept N numbers from user and store it into List. 
# Return Maximum number from that List.
# Description : Input : 1 2 3 4 5   Output : 5 
# =============================================================================

def main():
    Values = []
    Data = input("Enter the Values : ")

    while True:
        if Data == " ":
            break

        Values.append(int(Data))

    print(Values)


if __name__ == "__main__":
    main()