#Author : codingwithamar@gmail.com
#Description : 'Explain the use of the global keyword. When should it be used?'

value = 10

def display():
    print(value)    #Here, count is only being read, so the global keyword is not required.

def increment():
    global value
    value = value + 10  # except 20

def decrement():
    global value
    value = value - 5   #except 5

def main():
    display()
    increment()
    decrement()

    print(value)    #but answer is 15

if __name__ == "__main__":
    main()
