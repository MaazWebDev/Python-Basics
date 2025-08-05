# Question 2 : Movie Ticket Pricing
#  Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = 18
day = "Monday"

price = 12 if age >= 18 else 8

if day == 'Wednesday':
    price = price - 2
    # price -= 2

print('Welcome to Movie Threater, Today Is',day,'The Ticket Price For You is $',price)