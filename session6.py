"""
Closure
Decorator
Basic of rest framework
"""

x = 10
y = 20
print(x, y)


def greet(name):
    return f"Hello {name}"


print(greet("shyamji"))

say_hello = greet  # assign function to variable
print(say_hello)
print(say_hello("Alice"))  # Hello Alice

"""
inner function
"""

print("------------------------")


def outer():
    print("outside function")

    def inner():
        print("inside function")
        return "hey this is inner function"

    return inner()  # calling inner function


print(outer())  # calling outer function

print("----------------------------")
"""
(Closure)
"""


def outer():
    print("outside function closure")

    def inner():
        print("inside function closure")
        return "hey this is inner function closure"

    return inner  # calling inner function


func = outer()  # this will call outer fucntion and return inner function
print(func)
print(func())  # calling inner function

"""
closure with argument
"""
print("----------------------------")


def outer(x):
    print("outside function closure with args")

    def inner(y):
        print("inside function closure with args")
        return x + y

    return inner  # calling inner function


o = outer(10)
print(o)
print(o(20))

print("----------------------------")
"""
Python Decorators
A decorator is a function that takes another function as input, adds extra functionality,
 and returns a new function — without changing the original function’s code.
👉 It’s like “wrapping” one function inside another.
"""


def outer(greet):
    print("inside outer function")

    def inner():
        print("Before inside inner function")  # 4th print
        greet()  # this fucntion so we have to call it to use # 5th print
        print("After")  # 6 print

    return inner


def greet():
    print("Hi there")


out = outer(greet)  # first print
print(out)  # 2nd print
print(out())  # 3rd print
print("----------------------------")

"""
Decorator version
"""


def outer(greet):
    print("inside outer function decorator")

    def inner():
        print("Before inside inner function decorator")  # 4th print
        greet()  # this fucntion so we have to call it to use # 5th print
        print("After decorator")  # 6 print

    return inner


@outer
def greet():
    print("Hi there decorator")


print(greet())

print("------------------------------")


def outer(func): # func =def add(a, b):return a + b

    print("outer func") #1st

    def inner(a, b):
        print(f"inner with value {a} {b}") #3rd
        if a < 0 or b < 0:
            return "please provide positive number"

        return func(a, b) #  === def add(a, b):
                                    #  print("inside original function") #4
                                    # return a + b

    print(f"outside of inner") #2st
    return inner


@outer
def add(a, b):
    print("inside original function") #4
    return a + b


# print(add(5, 3))  # 8
print(add(-5, 3))  # Error: Negative values not allowed
