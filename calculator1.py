 #Message to the user
message = "Welcome to the calculator program\n"
print(message)

#getting input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#performing calculations
subtraction = num1 - num2
addition = num1 + num2
division = num1 / num2
modulus = num1 % num2
multiplication = num1 * num2

#Displaying results
print("the result of addition is:", addition)
print("the result of subtraction is: ", subtraction )
print("the result of division is: ", division )
print("the result of modulus is: ", modulus )
print("the result of multiplication is: ", multiplication)
