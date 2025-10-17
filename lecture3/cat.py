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
#\n is used to go to the next line
"""
print("meow\n"*3, end="")
"""
#this end thing is damn important without it it adds another extra line which makes it a little inefficient which we do not like.


#now we want a user input
"""
while True: #inducing an infinite loop delibritely
    n=int(input("what is n?"))
    if n<0:
        continue
    else:
        break
for i in range(n):
     print("meow")
"""

#now simplifying
"""
while True: #inducing an infinite loop delibritely
    n=int(input("what is n?"))
    if n>0:
        break

for _ in range(n):
        print("meow")
"""

def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n= int(input("what is n?"))
        if n>0:
            break
    return n

main()
