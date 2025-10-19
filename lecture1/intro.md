Functions, variables, conditionals, loops, exceptions, libraries, unit tests, file i/o, regular expressions, obejct oriented programming, additional tools and info


# lecture 1
## functions, variables

terminal- cli interface to the underlying pc 
computers only understands 0s and 1s 
so it is an interpretor-> name of file-> the interpretor will handle it 


functions- actions or verbs that allow u to do some action
humans can use functions to do those things
in hello.py the function is print

arguments- input to the function

side effect- the thing that appears on the screen 
bugs- mistakes in programs

can we write the code in word or excel?
- not the right tool to use
- vs code is the a general purpose text editor
- has colour 

is it possible to run the program without the terminal window?
- can be only run w the terminal window in this 
- you can write programs and allow users to use a gui or others

return values
variables- create a var is the computer's memory that stores a value like a container

in python a single = sign means assignment not necessarily equivalent

comments- hash symbol- write a note to urself
pseudocode- to write the intent of ur code- helps structure ur to-do list
input- expects string input 

many line comments """ fowhfjfpgf """

- when u pass multiple arguments in python it automatically inserts the space for you
- this is when u use the comma and not the addtion symbol (concatenation)

in case of string:- it is used for concatenation (+), can use for multiple arguments but is ugly.
strings- str

### print(*objects, sep=' ', end='\n', file=None, flush=False)
u can use '' or "" but just be consistent.

parameters- passing values to print- they are positional
they are optional, passed at the end of the print

what if we want to use "" within ""
- use '' outside and "" inside
- or put backslashes on the inner ""

format string or f string - tells python to format it 
- have to add f in the beginning of the quotes


method
- name.strip()- name of string+ period+ function+ parenthesis
- capitalize only makes first letter uppercase
- title will help capitalize each word


int 
- no decimal point
- +,-,*,/,%
- % modulo operator: takes the remainder

- int is not only a data type but also a function in python

interactive mode

## program calc
### first version of calculator 
this is more readable- so in that sense it is better

x = (input("what is x?"))
y = (input("what is y?"))  
z=int(x)+int(y) 
print(z)

### new way

x = int(input("what is x?"))
y = int(input("what is y?"))  #nested functions
print(x+y) 


float
- number with a decimal point
- mathematically, a real number

there is a function in python called round
- syntax- round(number[, ndigits]) 
- [] in syntax means optional

what to do if we want output to put 1,000 instead of 1000?
- use fstring
- print(f"{z:,}")


### def
- to define
- if and when we want to create functions using python, we can do so using def function
- if u want to call a function
- it should be defined on the top of the file
- for this problem we use main function
- scope: we can use a var of a function within a function, if needed we need to hand it to other functions
