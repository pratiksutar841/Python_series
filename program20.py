'''===================================================================================================='''
'''
Question-1: Print the given pattern
For n = 1
*****
For n = 2
*****
*****
For n = 3
*****
*****
*****

Print five stars in each row where no. of rows = n
'''
n = int(input("Enter the value of n: "))
 
for i in range(n):
    print("*" * 5)

'''===================================================================================================='''
'''
Question-2: Print the given pattern
For n = 4 for n=6
1234 123456
1234 123456
1234 123456
1234 123456
123456
123456
'''
n = int(input("Enter the value of n: "))
 
for i in range(n):
    for j in range(1, n + 1):
        print(j, end="")
    print()

'''======================================================================================================'''
'''
Question-3: Print the given pattern
For n = 4
*
**
***
****
'''
n = int(input("Enter the value of n: "))
 
for i in range(1, n + 1):
    print("*" * i)
'''======================================================================================================='''
'''
Question-4: Print the given pattern
For n = 4
1
1 2
1 2 3
1 2 3 4
'''
n = int(input("Enter the value of n: "))
 
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''========================================================================================================'''
'''
Question-5: Print the given pattern
     1
   1 2 3
 1 2 3 4 5
1 2 3 4 5 6 7
'''

n = int(input("Enter the value of n: "))
 
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''========================================================================================================='''