"""Explain how Python manages memory automatically.
Why does the programmer not need to explicitly allocate or free memory?"""

import sys

x = [10,20,30]

print("Address :", id(x))
print("Size    :", sys.getsizeof(x))

y = x

print("Same Address :", id(y))

del x

print(y)
print("Size    :", sys.getsizeof(y))