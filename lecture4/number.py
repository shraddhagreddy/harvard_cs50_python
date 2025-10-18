#printing an integer

"""
x=int(input("what is x?"))
print(f"x is {x}")

this does not work when a user enters a string or char
then this comes as output

what is x?cat
Traceback (most recent call last):
  File "/Users/shraddhagirishreddy/Desktop/harvard_python/lecture4/number.py", line 3, in <module>
    x=int(input("what is x?"))
ValueError: invalid literal for int() with base 10: 'cat'

invalid literal- whatever is timed in for int (to convert), base 10 is the decimal system 
we have to assume the user is going to make mistakes
not try and request them saying pls enter integer
"""

#indentation is important
try:
    x=int(input("what is x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")