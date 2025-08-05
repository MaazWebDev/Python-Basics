# Tuples:
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

myTuple = ("Red","Green","Blue")
print(myTuple)
print(type(myTuple))
print(len(myTuple))

# Access

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])

myTuple2 = ("Orange","Yellow")

# Join

allTuple = myTuple + myTuple2
print(allTuple)

for x in myTuple:
    print(x)

if "Red" in myTuple:
    print("Red AVailble")

# Coun

print(myTuple2.count("Orange"))