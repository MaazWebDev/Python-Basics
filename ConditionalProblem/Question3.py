# Question : 3. Grade Calculator
#  Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)

Marks = 100
if(Marks >= 101):
    print('Please Verify Your Marks Again')
    exit()

if Marks >= 90:
    grade = 'A'
elif Marks >= 80:
    grade = 'B'
elif Marks >= 70:
    grade = 'C'
elif Marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print('Grade :',grade)