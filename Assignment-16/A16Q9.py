# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A16Q9.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-16\A16Q9.py
# Subject : 9. Write a program which display first 10 even numbers on screen.
# Description : Output : 2 4 6 8 10 12 14 16 18 20
# =============================================================================

def main():
    count = 0
    num = 2
    
    while count < 10:
        print(num)
        num += 2
        count += 1

if __name__ == "__main__":
    main()
    