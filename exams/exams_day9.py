# t1 = (6,1,2)
# print(t1[0]/t1[2]*(t1[1]+t1[2]))

# tuple1 = (50, 10, 60, 70, 70)
# print(tuple1.count(50))


# tup1 = ('physics', 'chemistry', 1997, 2000)
# for value in range(0,3):
#     print(f"{value}: {tup1}")



# items = {"apple","orange","apple","orange","strawberry"}
# print(items[0])

# info = {"name": "john doe", "age": "20", "addres": "Pasay"}
# for a in info:
#     print(f"{info[a]} == {a}")


# import math
# print(math.randrange(1,10))

# try:
#     10/2
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except FileNotFoundError:
#     print("FileNotFoundError")
# else: 
#     print("No error")


# try: 
#     a = "orange"
#     if a == "apple":
#         raise ValueError
#     else:
#         raise TypeError
# except ValueError:
#     print("Apple Error")
# except TypeError:
#     print("Orange Error")
# else:
#     print("No Error")
# finally:
#     print("Fruit Error")


# print(int(math.sqrt(10)))
# import math
# a = math.sqrt(20)
# b = math.sqrt(30)
# print(int(a+b))

# class Person:
#     name = "John"

# p1 = Person()
# p2 = Person()
# p2.name = "Mike"
# print(p1.name)
# print(p2.name)


# class Person:
#     name = "John"
#     def sayHi (self):
#         print("Hi! " + self.name)
#     def sayHello (self):
#         print("Hello! " + self.name)
#     def greet (self):
#         print("Welcome " + self.name)
#         self.sayHi()
#         self.sayHello()
# p1 = Person()
# p1.greet()


# class Father:
#     eyes = "blue"
# class Mother:
#     hair = "brown"
# class Child(Father, Mother):
#     height = "175 cm"

# a = Child()
# print(a.eyes)
# print(a.hair)
# print(a.height)


# class Person:
    
#     def __init__(self, name, position):
#         self.empname = name
#         self.empposition = position
        
#     def isEmployed(self):
#         return False
    
# class Employee(Person):
    
#     def isEmployed(self):
#         return True

# emp1 = Employee("Vicent", "Musa")
# print('Employed?:', emp1.isEmployed())



class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printMessage(self):
        print("Name: " + self.name)
        print("Age: " + self.age)

t1 = Test()
t1.printMessage()