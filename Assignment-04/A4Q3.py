"""Predict the output:
lst = [10, 20, 30]
tpl = (10, 20, 30)
lst[0] = 100
tpl[0] = 100
Which line will raise an error and why?
"""
lst = [10, 20, 30]
tpl = (10, 20, 30)
lst[0] = 100
tpl[0] = 100    #This line genereates error because tuple is non mutable
