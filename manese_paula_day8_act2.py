# 1. Create a Class called Employee
# 2. Use the init function to collect the employee information (Name, email and mobile number)
# 3. Instantiate the Employee class two times with different information
# 4. Display all the properties of the object.


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def details(self):
        print("Employee Name:",  self.name)
        print("Employee Age:", self.age)
 
 
emp = Employee("Sam", 36)
emp.details()