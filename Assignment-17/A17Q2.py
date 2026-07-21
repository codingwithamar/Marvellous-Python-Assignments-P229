# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A17Q2.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-17\A17Q2.py
# Subject : 2. Write a program which accept one number and display below pattern.
# Description : Input : 5
#               Output : * * * * *
#                        * * * * *
#                        * * * * *
#                        * * * * *
#                        * * * * *
# =============================================================================

def main():
    print("Enter the Number :")
    Value = int(input())
    for i in range(Value):
        #print(" * " * Value)
        print(" ".join(["*"] * Value))

if __name__ == "__main__":
    main()
    