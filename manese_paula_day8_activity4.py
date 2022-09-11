# 1. Create House Class with the following properties and methods
# floorSize
# noOfFloors
# noOfDoors
# switchOn()
# lightOpen()
# ovenOpen()
# 2. Create TownHouse Class inherit the House class
# 3. Modify the value of the following(noOfFloors and noOfDoors)
# 4. Instantiate the TownHouse Class once
# 5. Display all the properties
# Calling the switchOn() will automatically execute lightOpen() and ovenOpen()


class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors

    def switchOn(self):
        print()
        print("\tSwitch ON")
        self.lightOpen()
        self.ovenOpen()
        print()
        print("\tEnd of Program")

    def lightOpen(self):
        print("\tLight Open")

    def ovenOpen(self):
        print("\tOven Open")


class TownHouse(House):
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        super().__init__(floorSize, noOfFloors, noOfDoors)

    def displayTownHouseProperties(self):
        print()
        print("\tHouse Floor Size    : ",self.floorSize)
        print("\tHouse No. of Floors :  ",self.noOfFloors)
        print("\tHouse No. of Doors  : ",self.noOfDoors)

TownHouse_One = TownHouse(320,3,5)
TownHouse_One.displayTownHouseProperties()
TownHouse_One.switchOn()