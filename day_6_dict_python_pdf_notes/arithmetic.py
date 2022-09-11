#Sample Code for Module
#arithmetic.py is the main file
#operations.py is the module

from operations import *

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print('The Sum is:', add(num1, num2))
print('The Difference is: ', subtract(num1, num2))
print(multiplication(num1, num2))