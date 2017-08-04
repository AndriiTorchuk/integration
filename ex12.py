"""
Exercise 12: My awesome calculator
"""

# import data from files
from ex4 import calc
from ex2 import textValue
from ex3 import *
from math import factorial

# Testing if this work correct
assert calc(1, 1) == 2

answer = [1, 2, 3, 4, 5, 6]
assert len(answer) > 5 

text = "quick fox jumps over a lazy dog"
assert "foxe" not in text  

assert len(textValue) > 0

i = 10
if myfactorial(i) == factorial(i):
    print ("it works")
else:
    print("It work  bad")
