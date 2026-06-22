"""
5. Predict the output:
a = 10
b = 10
print(id(a) == id(b))
Explain why this happens.
"""

a = 10
b = 10

print(id(a))
print(id(b))
print(id(a) == id(b))
print("\nHere a and b memory location is shared which is same.")