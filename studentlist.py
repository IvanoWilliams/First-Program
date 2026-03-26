#Working with lists
#List functions to add elements==> append(), insert()
#List functions to remove elements ==> remove(), pop()
#other list functions==> sort(), reverse()
print("=========")
print("\nHello , this Program lets you store and display students in\n")
print("=========")

num_of_students = int(input("Hello, please enter the number of students in your Class: \n"))

#create empty list
studentList = []

#range of the num_of_students
for y in range(num_of_students):
    name = input("Enter student details: ") 
    studentList.append(name)

#print the studentList
for x in studentList:
    print(x)