# Question 8. Password Strength Checker
# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = 'jwdcnjfcjc'

if len(password) < 6:
    strength = 'Weak'
elif len(password) <= 10:
    strength = 'Meddium'
else:
    strength = 'Strong'
print('You Password Strength Is',strength)