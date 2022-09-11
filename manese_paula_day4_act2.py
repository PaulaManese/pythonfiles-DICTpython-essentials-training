# Day 4 Act 2
# 1. Write a program that adds two numbers.
# 2. The program will ask to enter first and second number
# 3. The program will display “The sum of n1 and n2 is nTotal”
# 4. The program will ask if the user wants to try again. The user will input
# Y/y if Yes and N/n if No
# 5. If Yes, refer to step 2.
# 6. If No, the program will display “Thank you!”.




num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of {0} and {1} is {2}.".format(num1, num2, sum))
ans = input("Do you want to try again?: ")

while ans.upper() == "Y":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print("The sum of {0} and {1} is {2}." .format(num1,num2, sum))
    ans = input("Do you want to try again?: ")

print("Thank you!")
