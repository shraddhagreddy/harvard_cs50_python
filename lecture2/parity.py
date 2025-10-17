#now we will use % (modulo operator)
#gives the remainder

def main():
    x=int(input("what is x?"))
    if iseven(x):
        print("even")
    else:
        print("odd")

"""
def iseven(n):
    if n%2==0:
        return True #boolean values
    else:
        return False
"""

#do not need all 4 lines (pythonic)

""""
first appraoch

def iseven(n):
    return True if n%2==0 else False

"""

def iseven(n):
    return n%2==0

main()