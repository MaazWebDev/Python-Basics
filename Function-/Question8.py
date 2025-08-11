# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
      print(f"{key}: {value}")

print_kwargs(Name="Maaz",Expert="Python")
print_kwargs(Name="Mirza",Expert="Python1")
print_kwargs(Name="Mahad",Expert="Python2",Advanced="Ai")