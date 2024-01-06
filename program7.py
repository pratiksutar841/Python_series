# Taking input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
 
# Calculating the simple interest
interest = (principal * rate * time) / 100
 
# Displaying the output
print("\nThe Simple Interest is:", interest)