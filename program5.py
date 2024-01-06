'''----------------------------------------------------------------------------------------'''
# Arithmetic Operators

a = 10
b = 3
 
print("Sum:", a + b)              # Output: Sum: 13
print("Difference:", a - b)       # Output: Difference: 7
print("Product:", a * b)          # Output: Product: 30
print("Division:", a / b)         # Output: Division: 3.3333333333333335
print("Floor Division:", a // b)  # Output: Floor Division: 3
print("Modulus:", a % b)          # Output: Modulus: 1
print("Exponentiation:", a ** b)  # Output: Exponentiation: 1000

'''---------------------------------------------------------------------------------------'''
# Assignment Operators

a = 10
b = 3
 
a += b
print("Updated a (using +=):", a)  # Output: Updated a (using +=): 13
 
a -= b
print("Updated a (using -=):", a)  # Output: Updated a (using -=): 10

'''--------------------------------------------------------------------------------------'''
# Comparison Operators
a = 10
b = 3
 
print("a == b:", a == b)  # Output: a == b: False
print("a != b:", a != b)  # Output: a != b: True
print("a < b:", a < b)    # Output: a < b: False
print("a > b:", a > b)    # Output: a > b: True
print("a <= b:", a <= b)  # Output: a <= b: False
print("a >= b:", a >= b)  # Output: a >= b: True

'''----------------------------------------------------------------------------------------'''
# Logical Operators
a = 10
b = 3
 
print("a > 0 and b > 0:", a > 0 and b > 0)    # Output: a > 0 and b > 0: True
print("a > 0 or b > 0:", a > 0 or b > 0)      # Output: a > 0 or b > 0: True
print("not(a > 0):", not(a > 0))              # Output: not(a > 0): False

'''----------------------------------------------------------------------------------------'''
# Bitwise Operators
a = 10
b = 3
 
print("Bitwise AND:", a & b)    # Output: Bitwise AND: 2
print("Bitwise OR:", a | b)     # Output: Bitwise OR: 11
print("Bitwise XOR:", a ^ b)    # Output: Bitwise XOR: 9
print("Left Shift by 1:", a << 1)    # Output: Left Shift by 1: 20
print("Right Shift by 1:", b >> 1)   # Output: Right Shift by 1: 1

'''---------------------------------------------------------------------------------------'''

fruits = ['apple', 'banana', 'orange']
 #Membership Operators:
print("'apple' in fruits:", 'apple' in fruits)          # Output: 'apple' in fruits: True
print("'pear' not in fruits:", 'pear' not in fruits)  # Output: 'pear' not in fruits: True

'''---------------------------------------------------------------------------------------'''
# Identity Operators
x = 5
y = 5
 
print("x is y:", x is y)           # Output: x is y: True
print("x is not y:", x is not y)   # Output: x is not y: False

'''---------------------------------------------------------------------------------------'''