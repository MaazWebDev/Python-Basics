# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))
print(sum_all(1,2,3,4,5,6,7,8,9))