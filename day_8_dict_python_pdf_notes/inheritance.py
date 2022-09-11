class Person:
    
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    def isStudent(self):
        return False


class Student(Person):

    def isStudent(self):
        return True


class Grades:
    def __init__(self, math, science):
        self.mathgrade = math
        self.sciencegrade = science

    def printgrade(self):
        print(self.mathgrade, self.sciencegrade)


class StudRecord(Person, Grades):

    def __init__(self, fname, lname, math, science):
        self.firstname = fname
        self.lastname = lname
        self.mathgrade = math
        self.sciencegrade = science

    def printname(self):
        print('\n' + self.firstname,
              self.lastname + "\nMath Grade: " + str(self.mathgrade) + "\nScience Grade: " + str(self.sciencegrade))


person1 = Person("John", "Doe")
person1.printname()
print('Student?:', person1.isStudent())

person1 = Student("Vincent", "Musa")
person1.printname()
print('Student?:', person1.isStudent())

person1 = StudRecord("Vincent", "Musa", 80, 90)
person1.printname()