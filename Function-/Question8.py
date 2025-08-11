# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
      print(f"{key}: {value}")

print_kwargs(Name="Maaz",Expert="Python")
print_kwargs(Name="Mirza",Expert="Python1")
print_kwargs(Name="Mahad",Expert="Python2",Advanced="Ai")