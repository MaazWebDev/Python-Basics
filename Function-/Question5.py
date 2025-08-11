# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def greet(name = 'User'):
    return 'Hello ' + name + '!'

print(greet('Maaz'))
