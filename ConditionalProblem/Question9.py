# Question 9. Leap Year Checker
#  Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400)

year = 2025

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,'Is a Leap Year')
else:
    print(year,'Year Is Not A Leap Year')