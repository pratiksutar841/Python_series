# 1. Printing Text
print("Hello, World!")

# 2. Printing Variables
name = "Pratik"
age = 21
print("My name is", name, "and I am", age, "years old.")
''' Or we can also modify the print statement as:
 print("My name is" + name + "and I am" + age + "years old.") '''

# 3. Printing Expressions
x = 10
y = 5
print("The sum of", x, "and", y, "is", x + y)

# 4. Printing Formatted Strings
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 5. Printing with Separator
x = 1
y = 2
z = 3
print(x, y, z, sep="-") # Output: 1-2-3


# 6. Printing to a File
with open("output.txt", "w") as f:
 print("Hello, World!", file=f)


string = "€"
unicode_code = ord(string)
print("Unicode of", string, "=", unicode_code)
