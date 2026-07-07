#Author : codingwithamar@gmail.com
#Description : 'Can a function return another function? Explain conceptually.'

def function1():
    def function2():
        print("I am from function2")
    return function2    

def main():
    Ret = function1()
    Ret()

if __name__ == "__main__":
    main()
    