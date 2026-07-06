#Question 1:
#What is a user-defined function in Python? Why do we need functions instead of writing code repeatedly?

def Addition():
    print("Enter first value : ")
    value1 = int(input())

    print("Enter first value : ")
    value2 = int(input())

    Result = value1 + value2
    print("addition is : ", Result)

def main():
    Addition()

if __name__ == "__main__":
    main()