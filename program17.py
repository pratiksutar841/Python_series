for i in [1,2,3,4]:
 print(i)

'''=================================================================================='''
# Question: Print hello world ‘n’ times. Take ‘n’ as inXut from user.

n = int(input("Enter the value of n: "))
print()
for _ in range(n):
    print("Hello, World!")

'''=============================================================================='''

    # Question: Print numbers from 1 to 100
for num in range(1, 101):
    print(num)

'''===================================================================================='''
# Question: Print even numbers from 1 to 100

for num in range(2, 101, 2):
    print(num)

'''===================================================================================='''
# Question: Display this AP - 1,3,5,7,9.. upto ‘n’ terms.    

n = int(input("Enter the number of terms: "))
 
current_term = 1
common_difference = 2
 
print("\nAP:", end = " ")
for _ in range(n-1):
    print(current_term, end=", ")
    current_term += common_difference
print(current_term)


'''============================================================================'''
n = int(input("Enter the number of terms: "))
 
current_term = 1
common_difference = 2
end_term = current_term + (n-1)*common_difference
print("\nAP:", end = " ")
for _ in range(current_term, end_term, common_difference):
    print(current_term, end=", ")
    current_term += common_difference
print(current_term)