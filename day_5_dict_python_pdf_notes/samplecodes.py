def info(name,age):
    print(name + ', ' + str(age))
   
info('Vinz', 35)

def greet(name='Monkey D Luffy'):
    print('Hi', name)
    print('WELCOME!')
   
def greetings():
    return 'Hello to everyone!'
   
#print(greetings())

def SUM(num1, num2):
    total = num1 + num2
    return total, 'Vinz'

int1 = int(input('Enter first number:')) #15
int2 = int(input('Enter second number:')) #20
print(SUM(int1,int2))

#This is for the reversing the string
string1 = "REVERSED"
print(string1[::-1])