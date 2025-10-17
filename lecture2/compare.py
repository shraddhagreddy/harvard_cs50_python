x= int(input("what is x?"))
y= int(input("what is y?"))

"""
#this code is repetitive so its not v nice
#asking 3 questions irrespective is its right or not

if x<y:
    print("x is less than y")

if x>y:
    print("x is greater than y")

if x==y:
    print("x equals y")

"""

"""
#so now we'll use elif
#only asks te questions if i have not already gotten the answer
#logically better 
if x<y:
    print("x is less than y")

elif x>y:
    print("x is greater than y")

elif x==y:
    print("x equals y")
"""

#why even ask the last question
#logically it is not required, because there are only 3 possibilities

"""
if x<y:
    print("x is less than y")

elif x>y:
    print("x is greater than y")

else:
    print("x equals y")
"""


#or 
"""
if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

#to make the code better just use x!=y rather than x>y or x<y
#so basically:
if x!=y:
    print("x is not equal to y")
else:
    print("x is equal to y")



