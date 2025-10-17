
#basic approach
"""
students= ["Hermoine","Harry","Ron"]
print(students[0])
print(students[1])
print(students[2])
"""

#we are using student instead of _ as it is appropriate
#using for loop

"""
students= ["Hermoine","Harry","Ron"]
for student in students:
    print(student)
"""
#we cannot do range(students)- as it is not an integer
#we can use len instead

""""
students= ["Hermoine","Harry","Ron"]
for i in range(len(students)):
    print(i+1,students[i]) #added i+1 to show the rankings of the students
"""

#we can agree that as we go 0,1,2 on one list with the other- student lives in corresponding house
#break down quickly as we go 
#so not so good
""""
students= ["Hermoine","Harry","Ron"]
houses=["Gryffinfor","Gryffindor","Griffindor","Slytherin"]
"""

#so that is why we will use python dictionary
#we use curly braces
"""
students ={"Hermoine":"Gryffindor", 
           "Harry":"Gryffindor", 
           "Ron":"Gryffindor",
           "Draco":"Slytherin",
}

#here it is no 0,1,2 like in lists
#so we want the value of the key
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
"""

#now making it better
"""
students ={"Hermoine":"Gryffindor", 
           "Harry":"Gryffindor", 
           "Ron":"Gryffindor",
           "Draco":"Slytherin",
}

#if we use a for loop while iterating over a dict it always returns the key 

for student in students:
    #print(student) --> this will give you only the key

    #for loop will let me set student=hermoine first and then derives the value and so on...
    # instead of numeric location it iterates over the keys instead

    print(student,students[student], sep=", ")
"""

#now what if there is even more info then what?
#like adding patronus also
#students will be a list, and each student within that list will be a dictionary itself

students=[
    {"name":"Hermoine","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
] #list because[]
#within the list because {} dict

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


#if the dictionary is very huge and we want to search
#python will find it quickly- feature of python