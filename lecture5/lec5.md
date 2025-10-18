# Libraries

 - files of code others have written that u can use 
 - or files of code u have written in various of ur programs

 ## modules
 - library that has 1 or more functions
 - purpose of a library - encourage resusability of code

 - random library 
    - give functions that u dont have to access to otherwise
    - random.py - has one more functions that u can use : it is there when u download python

- import keyword
    - allows u to import the functions of the certain module

random.choice(seq)
- choice- function in random module
- random: module
- seq: list or listlike of something


from keyword
- while importing fucntions from module
- more specific


random.randint(a,b)->including a,b 
random.shuffle(x) - takes a list and shuffles them


## statistics library
- to calculate mean,median, mode, etc

## command-line arguments
- allows u to provide arguments (input to program) just while inputting at the command line
- ### sys
    - conatains a whole lot of functionality of the system
    - sys.argv (argument vector) - list of all the words human typed at prompt before enter

- ### slices
    - we can slice from the beginning or the end

- ### packages 
    - third party libraries
    - python has package which is a module
    - gain access to more functionality 
    - get it from pypi.prg
    - cowsay - package in python where we get to know what the cow says
    - pip - package manager
        - program that comes with python which allows u to install packages
        -  python3 -m pip install cowsay

what is the use of commad-line arguments? when it is less user-friendly?
- it is just not user-friendly for ppl not technical
- this make it more efficient


- ## APIS
    - not python specific 
    - third party services that u and i can wirte code that can talk to
    - apis live on the internet
    - ### package requests
        - allows u to make web requests using python code
        - most commonly used packages 
        - JSON
            - completely text based

- ## make our own libraries
    - bundle up the code you keep reusing
    - keep it local or open source