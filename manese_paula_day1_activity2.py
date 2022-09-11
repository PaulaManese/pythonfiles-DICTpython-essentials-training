#DAY1 1 -INTRODUCTION TO PYTHON
# 1. Create 5 Variables and use input function() to accept (Name (string),Math Grade (float),Science Grade (float),English Grade (integer), Average (float))
# 2. Assign appropriate value
# 3. Display the result:
# Name: __________
# Math Grade:_____________
# Science Grade:___________
# English Grade:___________
# Average:______________


math_grade = float(input("Please enter your Math Grade: "))
print("Math Grade:", math_grade)

science_grade = float(input("Please enter your Science Grade: "))
print("Science Grade:", science_grade)


english_grade = float(input("Please enter your English Grade: "))
print("English Grade:", english_grade)


average = (math_grade + science_grade + float(english_grade))
print("Average: " , float(average)/3)