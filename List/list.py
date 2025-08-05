# List :
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets: 

myList = ["App Developer","Python Developer","Website Developer","Ai Developer"]
print(myList)

# Type
print(type(myList))

# Index 
print(myList[0])
print(myList[1:3])
print(myList[-1])

color_List = ["Green","Blue","Red","Yellow"]
print(len(color_List))

if "Green" in color_List :
    print("Yes , We Have Color Green")

color_List[2] = "Purple";
print(color_List)

user_List = ["Maaz","Hasan","Ahmed","Ali"]
user_List[1:2] = ["Bilal","Faizan"]
print(user_List)

fruit_list = ["Mango","Grapes","Strawberry","Guava"]
fruit_list[1:3] = ["Water Melon"]
print(fruit_list)

# Insert()
fruit_list.insert(2,"Papaya")
print(fruit_list)


for item in fruit_list :
    print(item)

# Append ()

my_List = ["Jamshed","Haris","Bilal","Mubashir"]
print(my_List)
my_List.append("Hammad")
print(my_List)

# Pop()
my_List.pop()
print(my_List)

# Remove()

my_List.remove("Jamshed")
print(my_List)

# Copy()

my_List_copy = my_List.copy()
print(my_List_copy)

my_List_copy.append("Maaz")
print(my_List_copy)
print(my_List)

# Comprehension List

squared_num = [ x**2 for x in range(10)]
print(squared_num)

# Clear()
clear_list = ["Html","Css","Javascript"]
print(clear_list.clear())

# Sort()

car_list = ["Ford","Bmw","Volvo"]
print(car_list)
car_list.sort()
print(car_list)

number_list = [1,2,3,4,5,6,7,8,9]
print(number_list)
number_list.sort(reverse=True)
print(number_list)

# Sort the length wise car name
def myFunc(e) :
    return len(e)

car = ["Ford","Vm","Mitsubshi","Bmw"]
car.sort(key=myFunc)

print(car)


name_list = ["A","B","C"]
num_list = [1,2,3]

name_list.extend(num_list)
print(name_list)