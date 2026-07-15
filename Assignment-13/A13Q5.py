# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : A13Q5.py
# Path    : Marvellous-Python-Assignments-P229\Assignment-13\A13Q5.py
# Subject : 5. Write a program which accepts marks and displays grade. 
# Description : 
#               • ≥ 75 → Distinction 
#               • ≥ 60 → First Class 
#               • ≥ 50 → Second Class 
#               • < 50 → Fail
# =============================================================================

def Grade(Value):
    if Value >= 75 and Value <= 100:
        print("Your Grade is 'Distiction'")

    if Value >= 60 and Value < 75:
        print("Your Grade is '1st Class'")

    if Value >= 50 and Value < 60:
        print("Your Grade is '2nd Class'")
    
    if Value >= 35 and Value < 50:
        print("Your Grade is '3rd Class'")

    if Value >= 0 and Value < 35:
        print("Your Grade is 'Fail'")

def main():
    Marks = int(input("Enter the marks : "))
    Grade(Marks)

if __name__ == "__main__":
    main()
    