# ● Write a program that will compute for the students average
# ● The user will input the following:
# Name
# Math
# Science
# English
# ● If the average is equal and above 75 status is Passed else You Failed the semester



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