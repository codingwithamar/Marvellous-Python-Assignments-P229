"""Explain why strings are immutable in Python.
What happens internally when you modify a string variable?
"""

s = "hello"
print(id(s))        # 2277229153376

s = s + " world"
print(id(s))        # 2277229168368

#DIFFERENT id mean aloocate new object entirely..hence prove string is immutable

print("-----internal operations-------")
"""Step 1:  s = "hello"
        Memory: [addr_1] → "hello"
        s points to addr_1

Step 2:  s = s + " world"
        Python reads "hello" from addr_1
        Allocates NEW memory [addr_2] → "hello world"
        s now points to addr_2

        [addr_1] "hello" → still exists, 
        no longer referenced garbage collector will clean it up
"""
