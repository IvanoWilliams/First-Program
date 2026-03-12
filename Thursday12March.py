#Default login details stored in variables
username = "admin"
password = "admin@2026"

#Ask the user to enter their username
user_input = input("Enter username: ")

#Ask the user to enter their password
pass_input = input("Enter password: ")

#Check if both the username and password are wrong
if user_input != username and pass_input != password:
    print("Username and password is both wrong")

#check if only the username is wrong
elif user_input != username:
    print("Username is wrong")

#check if only the password is wrong
elif pass_input != password:
    print("Password is wrong")

#If both username and password are correct
else:
    print("You have successfully logged in")