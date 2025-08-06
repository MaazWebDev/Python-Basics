# Question 10. Pet Food Recommendation
# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = 'Dog'
age = 1

if species == 'Dog' and age < 2:
    food = 'Puppy Food'
elif species == 'Cat' and age > 5:
    food = 'Senior Cat Food'
else:
    food = 'Regular Food'
print('Feed Your',species,food)