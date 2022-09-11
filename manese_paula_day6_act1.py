

# 1. Create a Record Keeping App
# 2. The application will ask the user to choose between:
# a. Add Data
# b. Delete Data
# c. End
# 3. If Add data, the application will ask the
# user to input key and its value
# a. Enter Key: Lastname
# b. Enter Value: Doe
# 4. Store the information in a dictionary
# 5. Display the Result
# 6. If Delete Data, the application will ask for the key
# a. Enter Key: Lastname
# 7. Remove the item from the dictionary
# 8. Display the result
# 9. If End, display THANK YOU











print("******************************************")
print("         * Record Keeping App *           ")
print("******************************************")
print("Available Operators:")
print("A) Add Record\t\tB) View Record")
print("C) Clear Records\tD) Exit App\n")
print()
selection = str(input("Select an option [A,B,C,D]: "))

try:
    file = open("record.txt", "r")
except FileNotFoundError:
    file = open("record.txt", "x")

if selection.upper() == "A":
    var1 = str(input("Enter Name: "))
    var2 = str(input("Enter Email: "))
    var3 = str(input("Enter Address: "))
    file = open("record.txt", "a")
    file.write(f"\n{var1}, {var2}, {var3}")
    file.close()
elif selection.upper() == "B":
    file = open("record.txt", "r")
    print(file.read())
    file.close()
elif selection.upper() == "C":
    print("No records found.")
    file = open("record.txt", "r+")
    file.truncate(0)
    file.close()
elif selection.upper() == "D":
    print("Thank you")
else:
    print("Invalid input.")