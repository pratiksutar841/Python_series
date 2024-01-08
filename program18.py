# Question: Find the highest factor of given number ‘n’(excet n).

n = int(input("Enter a number: "))
highest_factor = -1
 
# Finding the highest factor
for factor in range(n-1, 0, -1):
    if n % factor == 0:
        highest_factor = factor
        break
 
# Printing the highest factor
print("The highest factor of", n, "is", highest_factor)
 