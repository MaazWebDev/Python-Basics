# Function 

# 1. Basic Function Syntax
# 2. Function with Multiple Parameters
# 3. Polymorphism in Functions
# 4. Function Returning Multiple Values
# 5. Default Parameter Value
# 6. Lambda Function
# 7. Function with *args
# 8. Function with **kwargs
# 9. Generator Function with yield
# 10. Recursive Function

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result

# In Python a function is defined using the def keyword:

def myfunction():
    print('Hello World')

# Argument :

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_function(fname):
  print("Hello " + fname)

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

