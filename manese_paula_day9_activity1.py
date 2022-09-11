# 1. Create a Record Keeping App
# 2. It will display the following options
# a. Add Record
# b. View Records
# c. Clear All Records
# d. Exit
# 3. If A: The user will input the following information (name, email, address)
# 4. The app will save the information in a text file.
# 5. If B, display the saved records
# 6. If C, clear the text file and display “No records found.”
# 7. If D, display “Thank you”




print("==========================================")
print("         ~ Record Keeping App ~")
print("==========================================")
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
