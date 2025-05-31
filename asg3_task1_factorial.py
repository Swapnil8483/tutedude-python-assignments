"""
#factorial using function recursion
"""

def factorial(num):
    if num <= 1:
        return 1
    else:
        num = num * (factorial(num - 1))
        return num

number = int(input("Enter a number to calculate factorial of: "))
result = factorial(number)
print (result)


'''
#factorial using while loop in function
'''

def factorial (num):
    fact = 1
    if num <= 1:
        return 1
    else:
        while num > 1:
            fact = fact * num
            num -= 1
        return fact

number = int(input("Enter a number to calculate factorial of: "))
result = factorial(number)
print (result)

'''
#factorial using for loop
'''

def factorial (num):
    if num <= 1:
        return 1
    else:
        for i in range(1,num):
            num = num * i
        return num

number = int(input("Enter a number to calculate factorial of: "))
result = factorial(number)
print (result)
