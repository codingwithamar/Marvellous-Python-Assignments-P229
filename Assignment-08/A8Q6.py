#Author : codingwithamar@gmail.com
#Description : 'Why is from module import * discouraged in professional code?'

from math import *
from math import *  #Name Comflicts
from cmath import * #sqrt() library define in math and cmath module 

def main():
    #1 NameSpace Pollution
    print(sqrt(25))
    print(pi)
    #After After this import, names like: sqrt, sin, cos, tan, log, pi, e

    #2 Name Comflicts
    print(sqrt(16)) #may overwrite the earlier one, making the code confusing.

if __name__ == "__main__":
    main()
    