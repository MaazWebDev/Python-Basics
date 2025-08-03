# Strings :

# Single Qoute String

firstString = 'Hello Python !'
print(firstString)
print(type(firstString))

# Double Q0ute Sring

secondString = "Hello Python 2 !"
print(secondString)
print(type(secondString))

# Triple Single Qoute String

thirdString = '''Hello ,  I am Python
I am Here To Help You
You Can You Me As You Need
Thank YOu !
'''

print(thirdString)
print(type(thirdString))

# Triple Double Qoute Sring

fourthString = """Hello ,  I am Python
I am Here To Help You
You Can You Me As You Need
Thank YOu !
"""

print(fourthString)
print(type(fourthString))

# Index Of []

fifthString = "Hello World" ;
print(fifthString) ;
first_char = firstString[0] ;
print(first_char)

# Slice 

sixthString = "Hello World 2"
print(sixthString)
slice_word = sixthString[0:5]
print(slice_word)

seventhString = "0123456789" ;
print(seventhString)

# Show ALL Value
numlist_1 = seventhString[:]
print(numlist_1);

# Start From Index 3
numlist_2 = seventhString[3:]
print(numlist_2);

# End at Index 7
numlist_3 = seventhString[:7]
print(numlist_3);

# Start From index 0 End at index 7 and After 2 Value
numlist_4 = seventhString[0:7:2]
print(numlist_4)

# String Methods :

# Lower()

eightString = "Python Developer";
print(eightString.lower())

# Upper()

ninthString = "python Developer";
print(ninthString.upper())

# Strip()

tenthString = "   Hello World    "
print(tenthString.strip())

#  Replace()

eleventhString = "Website Developer"
print(eleventhString.replace("Website","Python"))

# Split()

twevelthString = "Website Developer, App Developer, Python Developer";
print(twevelthString.split(","))

# Find()

thirtheenString = "Maaz Khan";
print(thirtheenString.find("K"))

# Count()

fourtheenString = "Bachelor Of Science In Artifical Intelligence"
print(fourthString.count("e"))

# Format()

project = "Ai Automation"
quantity = 2 ;
fiftheenString = "The Company Hire {} Developer for their {} project"
print(fiftheenString.format(quantity,project));

# Join()

sixtheenString = ["Maaz","BSAI","Python"]
print(", ".join(sixtheenString))

# Len()

seventheenString = "Hello World"
print(len(seventheenString))

for letter in seventheenString :
    print(letter)



eightheenString = "Maaz\nKhan"
print(eightheenString)

# Row String
ningtheenString = r"Maaz\nKhan"
print(ningtheenString)


twentyString = "Hello , I am \"Maaz Khan\" Doing BSAI From Ku";
print(twentyString)