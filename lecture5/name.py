#command-line argument
#sys

"""
import sys

print("hello, my name is ", sys.argv[1])
"""

"""
but we know from the beginning that index starts from 0
then we have mentioned 1 and it stores david
so what is in 0??
it has the name of the program
"""


#what is we dont enter the name?
"""
this error comes:
IndexError

shraddhagirishreddy@Shraddhas-MacBook-Pro lecture5 % python3 name.py      
Traceback (most recent call last):
  File "/Users/shraddhagirishreddy/Desktop/harvard_python/lecture5/name.py", line 6, in <module>
    print("hello, my name is ", sys.argv[1])
                                ~~~~~~~~^^^
IndexError: list index out of range

"""

#use exceptions now
"""
import sys
try:
    print("hello, my name is ", sys.argv[1])
except IndexError:
    print("too few arguments")
"""

#what is they give too many arguments?

"""
import sys
if len(sys.argv)<2:
    print("too few arguments")
elif len(sys.argv)>2:
    print("too many arguments")
else:
    print("hello, my name is ", sys.argv[1])
"""


#if we pass "david shraddha", then it works as it is passed as one

#refinement
"""
import sys
if len(sys.argv)<2:
    sys.exit("too few arguments")
elif len(sys.argv)>2:
    sys.exit("too many arguments")

print("hello, my name is ", sys.argv[1])
"""

#what if there are many name entered?

import sys
if len(sys.argv)<2:
    sys.exit("too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)

#but this gives even the name of the file