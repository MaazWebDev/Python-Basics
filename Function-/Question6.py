# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.


def cubeNum(num):
    return num ** 3

print(cubeNum(5))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

cube = lambda x: x ** 3

print(cube(3))