full_name = input("Please enter your Full Name: ")
working_hours =int(input("Please enter of hours: "))
sss_contribution = int(input("SSS contribution: "))
philhealth_contribution = int(input("PhilHealth contribution: "))
housing_loan= int(input("Housing loan: "))
rate_per_hour= 500
gross_salary = rate_per_hour * working_hours
other_loan = 100
tax = gross_salary * 0.10
total_deductions = sss_contribution + philhealth_contribution + other_loan + tax 
net_salary = gross_salary - total_deductions
print("=====================PAYSLIP===========================")
print("=============EMPLOYEE INFORMATION=======================")
print("Name: " , full_name)
print("Enter Number Of Hours:", working_hours)
print("Phil Health: " , philhealth_contribution)
print("Housing Loan: " , housing_loan)
print("Rate Per Hour: " ,rate_per_hour)
print("Gross Salary: " ,gross_salary)
print("======================DEDUCTIONS=======================")
print("SSS: " , sss_contribution)
print("Phil Health: " , philhealth_contribution)
print("Other Loan: " , other_loan)
print("Total Deductions: " , total_deductions)
print("Net Salary: " , net_salary)


# Formula:
# Tax = GrossSalary * 10%
# RatePerHour = 500
# GrossSalary = RatePerHour * Hour
# TotalDeductions = SSS + PhilHealth + OtherLoan + Tax
# NetSalary = GrossSalary - TotalDeductions