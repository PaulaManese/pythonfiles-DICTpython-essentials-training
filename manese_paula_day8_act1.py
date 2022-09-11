# 1. Create a class called Cellphone. The Cellphone class has the following fields:
# Color
# Manufacturer
# Model
# 2. Instantiate the Cellphone class 5 times
# 3. Modify the properties
# 4. Display all the properties



class Phone:
    
    # create class attributes
    name = "iPhone"
    make = "Apple"
    model = 2022

    # create class methods
    def start(self):
        print ("Hello welcome!")

    def stop(self):
        print ("Turn off")
            
    def call(self):
            print ("Calling..")

    def camera(self):
        print ("Open camera")
        
    def alarm(self):
            print ("Snooze")

