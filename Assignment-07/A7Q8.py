#Author : codingwithamar@gmail.com
"""Description : Explain what happens to __name__:
• When a Python file is executed directly
• When the same file is imported as a module"""

def add(a, b):
    return a + b

print("__name__ =", __name__)

if __name__ == "__main__":
    print("Calculator is running directly.")
    print("10 + 20 =", add(10, 20)) 