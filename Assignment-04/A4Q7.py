"""Predict the output:
d = {1: "One", 1: "ONE", 2: "Two"}
print(d)
Why does this happen?
"""


d = {1: "One", 1: "ONE", 2: "Two"}
print(d)

#OUTPUT :
#{1: 'ONE', 2: 'Two'}

#here 3 key value pair in dictionary, 1st two key is same but values are different and 3rd key 
#value is unique, according to dict rules key key are unique and values allowed to duplicates