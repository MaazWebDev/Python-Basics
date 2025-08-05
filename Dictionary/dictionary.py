# Dictionary :
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

thisDict = {
    "name" : "Grande",
    "brand" : "Toyota",
    "year" : 2025
}

print(thisDict)
print(type(thisDict))
print(len(thisDict))

thisDict2 = {
    "Name" : "Axio",
    "Hybrid" : False,
    "Model" : 2020,
    "Color" : ["Red","Green","Blue"]
}
print(thisDict2)
print(type(thisDict2))

# Accesss

print(thisDict2["Name"])
x = thisDict2.get("Model")
print(x)

# Key()

print(thisDict2.keys())

# Values()

print(thisDict2.values())

# Items()

print(thisDict2.items())

if "Model" in thisDict2 :
    print('Yes Available!')

# Change / Update

thisDict2["Model"] = 2021
print(thisDict2)

thisDict2.update({"Hybrid":True})
print(thisDict2)

for x in thisDict2 :
    print(x,thisDict2[x]) 

# Keys is x and value is dictionary

for key , value in thisDict2.items():
    print(key,value)

if "Name" in thisDict2 :
    print("Yours Car is Here")

# Add

myDict = {
    "userName" : "MaazKhan",
    "employeeId" : 176823,
    "underGraduate" : True
}
print(myDict)

myDict["Age"] = 20
print(myDict)

myDict.update({"Country":"Pakistan"})
print(myDict)

# Remove

myDict.pop("Age")
print(myDict)

myDict.popitem()
print(myDict)

del myDict["employeeId"]
print(myDict)

# del myDict;
# print(myDict)

myDict2 = {
    "Name" : "Maaz Khan",
    "Gender" : "Male"
}

# Copy

myDict_Copy = myDict2.copy()
print(myDict_Copy)

# Nested Dictionaries

carCompany = {
    "Corolla":{"Model":2023,"Trasmission":"AutoMatic"},
    "City":{"Model":2022,"Trasmission":"Manual"},
    "Shark 6":{"Model":2025,"Trasmission":"AutoMatic"},
    "Elantra":{"Model":2024,"Trasmission":"Manual"}
}
print(carCompany)

# Access

print(carCompany["Corolla"])

print(carCompany["Elantra"]["Model"])

# Loop

for x, obj in carCompany.items():
  print(x , obj);

  for y in obj:
    print(y + ':', obj[y])

keys = {"Name","UserName","DisplayName"};
default_values = "Maaz";

newDict = dict.fromkeys(keys,default_values)
print(newDict)