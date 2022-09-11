from day_6_dict_python_pdf_notes.manese_paula_day1_activity2.SalaryDeductions import tax, rate, TotalDeductions
from day_6_dict_python_pdf_notes.manese_paula_day1_activity2.NetSalary import net

name = str(input("Enter Name: "))
hour = int(input("Hour: "))
gross = rate(hour)

print()
print("Gross Salary:", gross)

print()
print("Tax:", tax(gross))
loan = float(input("Loan: "))
insurance = float(input("Insurance: "))
deductions = TotalDeductions(tax(gross), insurance, loan)
print()

print("Total Deduction: ", deductions)
print()
print("Net Salary: ", net(gross, deductions))