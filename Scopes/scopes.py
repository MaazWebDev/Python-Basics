# Scopes And Closure

username = 'Maaz Khan'


def func():
    # username = 'BsAi'
    print(username)

print(username)
func()


x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(4)
# print(result)

# def func3():
#     global x
#     x = 12

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def bsAi(num):
    def mainFunc(x):
        return x ** num
    return mainFunc

g = bsAi(2)
f = bsAi(4)

print(g(2))
print(g(4))