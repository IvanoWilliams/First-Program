 #This is a program that asks a user
#for their name, surname ,age current_year then prints
#a message that says Hello name surname, you were
#born in year_of_birth


#Message to the user
message="Hello Nerd, \"Welcome\" to Python\n"
print(message)

#Getting input from user
name = input("Enter your First Name: ")
surname = input("Enter your surname: ")
age=int (input("Enter your age: "))
current_year=int(input("Enter the current e.g 2026: "))

#Processing-Calculating the year_of_birth
year_of_birth = current_year-age

#Output-Display a message
print("Hello", name, " ", surname, "you were born in", year_of_birth)

