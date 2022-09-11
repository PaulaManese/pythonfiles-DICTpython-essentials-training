class Car:
    color = 'red'
    model = 'SUV'
    manufacturer = 'Toyota'

truck = Car()
van = Car()
jeepney = Car()

print('The colour of the Truck is:', truck.color)
print('The model of the Truck is:', truck.model)
print('The manufacturer of the Truck is:', truck.manufacturer)

print('\nThe colour of the Van is:', van.color)
vancolor = input("Enter color of Van: ")
van.color = vancolor
van.model = 'grandia'
van.manufacturer = 'Honda'
print('The colour of the Van is:', van.color)
print('The model of the Van is:', van.model)
print('The manufacturer of the Van is:', van.manufacturer)