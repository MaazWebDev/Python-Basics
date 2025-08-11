# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.


def cubeNum(num):
    return num ** 3

print(cubeNum(5))

cube = lambda x: x ** 3

print(cube(3))