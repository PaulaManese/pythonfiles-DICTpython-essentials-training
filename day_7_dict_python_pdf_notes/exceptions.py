try:
    result = 100 / 2
except ZeroDivisionError:
    print("Division by zero is error!")
except:
    print("Invalid input!")
else:
    print('No exceptions.\nDisplay the result is: ', result)

finally:
    print('Copyright @ 2022')