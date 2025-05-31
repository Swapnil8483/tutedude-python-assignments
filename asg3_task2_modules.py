from math import *

def calculations(num):
    sqr_root = sqrt(num)
    logarithm = log(num)
    cal_sine = sin(num)
    return sqr_root, logarithm, cal_sine

a = int(input("Enter a number :"))
result, result1, result2 = calculations(a)
print(f"Square root of {a} is {result}")
print(f"Logarithm of {a} is {result1}")
print(f"sine of {a} is {result2}")