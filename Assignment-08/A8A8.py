#Author : codingwithamar@gmail.com
#Description : 'What happens internally when Python executes an import module_name statement?'

import calculator

def main():
    print("Program Started")
    print("Import Completed")
    
    print(calculator.add(10, 20))
    print(calculator.PI)

    print("Program Finished")

if __name__ == "__main__":
    main()
        