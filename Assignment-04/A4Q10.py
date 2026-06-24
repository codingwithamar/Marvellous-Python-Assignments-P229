"""
What is the difference between:
range(1, 10)
range(1, 10, 2)
Explain the parameters.
"""

a = range(1, 10)        #(Start, Stop, Default 1)
b = range(1, 10, 2)     #(Start, Stop, Steps 2)

print(list(a))      #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(b))      #[1, 3, 5, 7, 9]