"""
print("#")
print("#")
print("#")
"""

#use for loop to make it more efficient
"""
for _ in range(3):
    print("#")
"""
#we are now going to use functions
"""
def main():
    print_column(3)

def print_column(height):
    for _ in range(3):
        print("#")

main()
"""

#smarter approach
"""
def main():
    print_column(3)

def print_column(height):
    print("#\n"*height, end="")

main()  
"""

#now we get coins
"""
def main():
    print_row(4)

def print_row(n):
    for i in range(n):
        print("? ",end="")

main() 
"""
#another approach
"""
def main():
    print_row(4)

def print_row(n):
    print("?"*n)

main() 
"""

#now we want to print a square which has width and height- and within each row
#there are 3 other squares
#outer loop- rows (size)
#inner loop- brick 

"""
def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#",end="") #do not want to move to next line
        print() #all by itself because we want to go to next line


main() 
"""


#tightening the code

"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#"*size) 

main() 
"""

#abstraction of the code
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    for i in range(width):
        print("#",end="")
    print()

main() 
