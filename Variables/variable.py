# Varibale :
# What Are Variables And How Variables Are Decalred And Initialized In Python
#  Variables are containers for storing data values.

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

name = "Maaz Khan";
print(name);
print(type(name))

age = 20 ;
print(age);
print(type(age))

a , b , c = "Html" , "Css" , "Javascript" ;
print(a)
print(b)
print(c)

# Global Variable
x = "Awesome";

def myFunc():
    print("Python is " + x)

myFunc();

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.