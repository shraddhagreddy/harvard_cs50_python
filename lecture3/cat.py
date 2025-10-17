"""
i=3
while i!=0:
    print("meow")
    i-=1
"""

#or another approach to the same problem
#no ++ or -- option like c
"""
i=1
while i<=3:
    print("meow")
    i+=1
"""

#for loop
""""
for i in [0,1,2]:
    print("meow")
"""
#how is this poorly designed?
#- it becomes an issue again with a list of large numbers[0,1,2...1,000,000]- makes no sense

#the better way
#using range
""""
for i in range(3):
    print("meow")
"""
#so u can literally just say range(1000000)
#minor improvement u can name a variable _ instead of an i, if it does not matter to you 


#if u really want to be pythonic 
print("meow\n"*3)