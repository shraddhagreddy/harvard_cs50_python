#importing module

"""
import random

coin=random.choice(["heads","tails"])
print(coin)
"""

#now being more specific 

"""
from random import choice

coin = choice(["heads","tails"])
print(coin)

#we can use the same functions that is in the random module- making it more specific
#without risking calling a function from the random module
"""

#sometimes better to do the first

""""
import random

number= random.randint(1,10)
print(number)
"""


#shuffling
import random

cards=["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)