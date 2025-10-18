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

"""
try:
    x=int(input("what is x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

again this is not the best practice as 
x=int(input("what is x?"))
    print(f"x is {x}")

is taking two lines so instead
"""



"""
try:
    x=int(input("what is x?"))
except ValueError:
    print("x is not an integer")
print(f"x is {x}")


now this error shows
we are getting NameError

what is x?cat
x is not an integer
Traceback (most recent call last):
  File "/Users/shraddhagirishreddy/Desktop/harvard_python/lecture4/number.py", line 41, in <module>
    print(f"x is {x}")
                  ^
NameError: name 'x' is not defined


why is not defined eventhough we have tried to define it on line2
- order of operations is wrong
- input function is working
- if passing that string to int function as argument
- it is prolly int function is creating an error
- the int(...) isnt working so no value is copied into x
- how to solve?
"""
#else

"""
try:
    x=int(input("what is x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
"""
#loops

"""
while True:
    try:
        x=int(input("what is x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
"""

#another approach
""""
while True:
    try:
        x=int(input("what is x?"))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is {x}")
"""

#trying to get number from user quite a bit

#always write the called function and then main
#actually ur wish 

""""
def main():
    x= get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x=int(input("what is x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    # in a function we need return something to be used later
    return x

main()
"""


#refinement

""""
def main():
    x= get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("what is x?"))
        except ValueError:
            print("x is not an integer")

main()
"""


#using pass
#makes it user-friendly

"""
def main():
    x= get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("what is x?"))
        except ValueError:
            pass

main()
"""

#refinements
#more dynamic- doesnt need to know what it is being asked for

def main():
    x= get_int("what is x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()


#there is also raise
