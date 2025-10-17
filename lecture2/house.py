name= input("whats ur name?")

"""
if name=="Harry":
    print("Griffindor")
elif name=="Hermoine":
    print("Griffindor")
elif name== "Ron":
    print("Gryffindor")
elif name=="Draco":
    print("Slytherin")
else:
    print("who?")

"""
#use or instead
"""
if name=="Harry"or name=="Hermoine" or name== "Ron":
    print("Griffindor")
elif name=="Draco":
    print("Slytherin")
else:
    print("who?")
"""

#now we will use match
match name:
    case "Harry" | "Hermoine"| "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
#do not need break or default statement just use the _ as a catch all statement
