# 1. Write a Python program to reverse a string
# 2. The user will input a word
# 3. Create a function that will reverse the string.
# 4. Display the original word, the reversed word in all caps and string count.
# 5. Save your file as lastname_firstname_day5_act2.py

# INPUT: Hello World
# OUTPUT: DLROW OLLEH (11 characters)



def reverse_string(word):
    return word[::-1]

string = input("Enter a string: ")
print(string)
print(reverse_string(string.upper()))
print("String count: ", len(string))
