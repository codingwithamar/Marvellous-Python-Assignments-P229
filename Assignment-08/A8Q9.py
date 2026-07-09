#Author : codingwithamar@gmail.com
#Description : 'What happens if a module contains print statements outside any function?'

print("Program Started")

import calculator

print("Import Finished")

result = calculator.add(10, 20)

print("Result =", result)

print("Program End")