#Author : codingwithamar@gmail.com
#Description : 'What are the different ways to import a module? Which one is recommended and why?'

#Module 1
import math

print(math.sqrt(25))
print(math.pi)

#Module 2
import math as m

print(m.sqrt(16))
print(m.pi)

#Module 3
from math import sqrt

print(sqrt(49))

#Module 4
from math import sqrt, pi

print(sqrt(64))
print(pi)

#Module 5
from math import *

print(sqrt(81))
print(pi)


