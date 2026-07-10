#Author : codingwithamar@gmail.com
#Description : '3. Write a program which accepts one number and prints factorial of that number.
#Input: 5
#Output: 120'

def factorial(num):
    total = 1
    for i in range(num, 0, -1):
        total = i * total
    print(f"Factorial of ", num, "is", total)

def main():
    print("Enter The number : ")
    NaturalNumber = int(input())
    factorial(NaturalNumber)

if __name__ == "__main__":
    main()
    