# Question 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for x in items:
    if x in unique_item:
        print('Duplicate : ', x)
        break
    unique_item.add(x)