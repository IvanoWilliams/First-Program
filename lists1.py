#Working with lists
#List functions to add elements==> append(), insert()
#List functions to remove elements ==> remove(), pop()
#other list functions==> sort(), reverse()
print("=========")
print("\nHello , this Program lets you store and display students in\n")
print("=========")

num_of_students = int(input("Hello, please enter the number of students in your Class: \n"))

#craete empty list
studentList = []

studentList.append("Ivano")
studentList.insert(0,"Aidan")
studentList[1] = "Lucin"

for y in range(0,num_of_students):
    studentList[y] = input("Enter student details: ") 


    for x in studentList:
        print(x)