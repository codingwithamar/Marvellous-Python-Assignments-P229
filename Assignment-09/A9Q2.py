#Author : codingwithamar@gmail.com
#Description : 'Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.'

def ChkGreater():
    a, b = map(int, input("Enter Two Numbers : ").split())
    print(type(a))
    if  a > b:
        print("a is greater : ", a)
    else:
        print("b is greater : ", b)

def main():
    ChkGreater()

if __name__ == "__main__":
    main()
    