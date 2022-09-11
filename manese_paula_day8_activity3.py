# 1. Create an app that computes students average
# 2. The user will input the following (Name, Math, Science and English Grade)
# 3. Create a Class called Students
# 4. Use the init function to collect the student information (Name, Math, Science and English Grade)
# 5. Create a function that will perform the computation of the average
# 6. Create a function that will display the result

# SAMPLE OUTPUT:
# Name: John
# Math: 90
# Science: 90
# English: 90
# Average: 90 (Passed)

class Students:
    def __init__(self, name, math, science, english):
        self.pangalan = name
        self.matematika = math
        self.agham = science
        self.ingles = english

    def ave(self):
        self.average = (self.matematika + self.agham + self.ingles) / 3

    def show(self):
        self.ave()
        print("Name: ", self.pangalan)
        print("Math Grade: ", self.matematika)
        print("Science Grade: ", self.agham)
        print("English Grade: ", self.ingles)
        if self.average >= 75:
            self.status = "Passed"
        else:
            self.status = "Failed"
        print("Average Grade: {} ({})".format(round(self.average,0), self.status))

print()
print("Student Average Grade Using Classes in Python")
print()
Name = str(input("Enter Name: "))
Math = float(input("Enter Math: "))
Science = float(input("Enter Science: "))
English = float(input("Enter English: "))
print()

stud = Students(Name, Math, Science, English)
stud.show()