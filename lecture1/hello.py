#ask user for their name and greet them
name = input("What's your name? ").strip().title()


#split user's name into first and last name
first,last = name.split(" ")

"""#remove white space from str
name = name.strip()

#capitalize user's name 
name = name.capitalize()
name = name.title()

#we can do both as well
name = name.capitalize().strip()"""


#or we can just do this
print("hello,", name)

#say hello to the user
print("hello,", name)


print("helloo, ", end ="")
print(name)

print("hello,", name, sep="???")


print("hello, \"friend\"")

print(f"hello, {first}")