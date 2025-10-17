"""

x = float(input("what is x?"))
y = float(input("what is y?"))  #nested functions

#z=int(x)+int(y) - initial what we did 
z=round(x+y)


#print(round(z)) 
print(f"{round(z):,}")


"""
"""
#now division

x = float(input("what is x?"))
y = float(input("what is y?"))  #nested functions

#round it to 2 decimal places
z=round(x/y,2) 
print(z)

# the comma helps with large numbers and the .2f helps with decimal places
print(f"{z:,.2f}")

"""


def main():
    x= int(input("what is the value of x?"))
    print("the square of x is",square(x))

def square(n):
    return n*n
    #can also use n**2 
    #can also use pow(n,2)

main()