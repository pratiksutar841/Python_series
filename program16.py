# Ternary Operator
# Question: Write a program to check if number is odd or even using ternary operator.

# Taking input number from the user
number = int(input("Enter a number: "))
 
# Checking if the number is odd or even using a ternary operator
result = "Odd" if number % 2 != 0 else "Even"
 
# Printing the result
print("The number is", result)
