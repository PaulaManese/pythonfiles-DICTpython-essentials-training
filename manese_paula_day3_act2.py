# ● Write a program that will check the employees years in service and office.
# ● The user will input number for years and in service and the following offices (IT, ACCT, HR)
# ● Check the following conditions


year = int(input('Please enter the years: '))
office = input('Please enter the office name: ')

print("\nsalary based on year/exp: ",end='')
if office.upper() == "IT" or office.lower() == "it":
    if year >=10: print(10000)
    else: print(5000)
elif office.upper() == "ACCT" or office.lower() == "acct":
    if year >=10: print(12000)
    else: print(6000)
elif office.upper() == "HR" or office.lower() == "hr":
    if year >=10: print(15000)
    else: print(7500)
else:
    print("The wrong office name entered")