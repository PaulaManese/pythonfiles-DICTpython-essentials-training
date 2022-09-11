# 1. Write a program that computes students average
# 2. Use a function with 4 parameters (Name, Math, English and Science Grade)
# 3. Reference the function 3 times with different values
# 4. Save your file as lastname_firstname_day5_act1.py

# Output
# John’s grade (Math=?, Science=?, English=?) and the average is ?
# Ana’s grade (Math=?, Science=?, English=?) and the average is ?
# Frank’s grade (Math=?, Science=?, English=?) and the average is ?

def Average(Name,Math,English,Science):
   solve = int(Math+English+Science)/3
   print("{0}'s grade (Math={1}, Science={2},English={3}),and the average is {4}."
         .format(Name,Math,English,Science,round(solve)))

print()
Average("John",99,95,98)
print()
Average("Ana",98,96,95)
print()
Average("Frank",97,98,96)