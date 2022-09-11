class Person:
    # constructor
    def __init__(self, name, age, height):
        # private data members
        self.__PName = name
        self.PAge = age
        self.PHeight = height

    def displayAge(self):
        # accessing public data member
        print("Age: ", self.PAge)

# creating object of the class
obj = Person("Naruto", 20, "165cm")
# accessing private data member
print("Name: ", obj._Person__PName)
# calling public member function of the class
obj.displayAge()