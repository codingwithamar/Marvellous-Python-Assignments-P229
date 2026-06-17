"""
4. What is the purpose of getsizeof()? 
Why is memory size different for different data types?
"""

import sys

x = 10
y = 3.14
name = "Python"

print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(name))
print("\n\n")

print(sys.getsizeof(10))
print(sys.getsizeof(3.14))
print(sys.getsizeof(True))
print(sys.getsizeof("Python"))
print(sys.getsizeof([10,20,30]))