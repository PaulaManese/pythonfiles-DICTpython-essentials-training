class Person:
    # constructor
    def __init__(self, name, age, height):
        # protected data members
        self._PName = name
        self.PAge = age
        self.PHeight = height

    def displayAge(self):
        # accessing public data member
        print("Age: ", self.PAge)

# creating object of the class
obj = Person("Naruto", 20, "165cm")
# accessing protected data member
print("Name: ", obj._PName)
# calling public member function of the class
obj.displayAge()