'''====================================================================================='''
# Question 1: Take positive integer input and tell if it is a four digit number or not.

# Taking positive integer input from the user
number = int(input("Enter a positive integer: "))
 
# Checking if the number is a four-digit number
if number >= 1000 and number <= 9999:
    print(f"\n{number} is a four-digit number.")
else:
    print(f"\n{number} is not a four-digit number.")
    
'''====================================================================================='''
# Question 2: Take positive integer input and tell if it is divisible by 5 and 3.

# Taking positive integer input from the user
number = int(input("Enter a positive integer: "))
 
# Checking if the number is divisible by both 5 and 3
if number % 5 == 0 and number % 3 == 0:
    print("The number is divisible by both 5 and 3.")
else:
    print("The number is not divisible by both 5 and 3.")

'''====================================================================================='''
# Question 3: Take positive integer input and tell if it is divisible by 5 or 3.

# Taking positive integer input from the user
number = int(input("Enter a positive integer: "))
 
# Checking if the number is divisible by 5 or 3
if number % 5 == 0 or number % 3 == 0:
    print("The number is divisible by 5 or 3.")
else:
    print("The number is not divisible by 5 or 3.")

'''======================================================================================'''
# Question 4: Take 3 positive integers input and print the greatest of them.

    # Taking three positive integer inputs from the user
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
 
# Comparing the numbers to find the greatest
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
 
# Printing the greatest number
print("\nThe greatest number is:", greatest)

'''======================================================================================='''
#Question 5: Determine whether the year is a leap year or not.
# Taking a year input from the user
year = int(input("Enter a year: "))
 
# Checking if the year is a leap year
print()
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

'''========================================================================================'''
# Question 6: Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.

# Taking positive integer input from the user
number = int(input("Enter a positive integer: "))
 
# Checking divisibility conditions using nested if-else
if number % 15 == 0:
    print("The number is divisible by 15.")
else:
    if number % 5 == 0 or number % 3 == 0:
        print("The number is divisible by 3 or 5 but not by 15.")
    else:
        print("The number is neither divisible by 3 nor by 5.")

'''========================================================================================='''
# Question: Take 3 positive integers input and print the greatest of them (without using multiple condition)

# Taking three positive integer inputs from the user
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
 
# Comparing the numbers to find the greatest using nested if-else
if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3
 
# Printing the greatest number
print("\nThe greatest number is:", greatest)

'''============================================================================================='''
'''Question: Take input percentage of a student and print the Grade according to marks:
1) 81-100 Very Good
2) 61-80 Good
3) 41-60 Average
4) <=40 Fail'''

# Taking the percentage input from the student
percentage = float(input("Enter the percentage: "))
 
# Determining the grade based on the percentage using elif
if percentage >= 81:
    grade = "Very Good"
if percentage >= 61 and percentage <= 80:
    grade = "Good"
if percentage >= 41 and percentage <= 60:
    grade = "Average"
if percentage <= 40:
    grade = "Fail"
 
# Printing the grade
print("Grade:", grade)

# Taking the percentage input from the student
percentage = float(input("Enter the percentage: "))
 
# Determining the grade based on the percentage using elif
if percentage >= 81:
    grade = "Very Good"
elif percentage >= 61:
    grade = "Good"
elif percentage >= 41:
    grade = "Average"
else:
    grade = "Fail"
 
# Printing the grade
print("Grade:", grade)
'''========================================================================================'''