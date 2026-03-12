 #Using operators

#Example 1 checking for equality
a = 10
b = 15

print("Equality a==b: ", a==b)
print("Not equal to a!=b",a!=b)

#Using Modulus - Getting the remainder after division

num1 = 5
num2 = 2

#Finding modulus
remainder = num1 % num2

print("The remainder from num1 % num2: ", remainder)

#Checking if a number from the user is even or odd

#inputNum = int(input("Enter any number: "))
#rem = inputNum % 2

#if rem==0:
 #   print("The number you entered is even")
#else:
 #   print("The number is not even")

 #Grading Application based on mark entered by user  

mark = float(input("Please enter Mark"))

if (mark>=0) and mark<=49:
    print("FAIL")
elif mark>=50 and mark<=59:
    print("PASS")   
elif mark>=60 and mark<=69:
    print("PASS+")    
elif mark>=70 and mark<=100:
   print("Distinction")    
else:
    print("Mark should be between 0 and 100 inclussive")   