import sys

from sayings import hello

if len(sys.argv)==2:
    hello(sys.argv[1])

#this error comes
"""
shraddhagirishreddy@Shraddhas-MacBook-Pro lecture5 % python3 say1.py david
hello, world
goodbye, world
hello, david


to correct this,
dont call main outside unconditionally 
"""