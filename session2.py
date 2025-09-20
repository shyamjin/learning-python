"""def apply_twice(func, x):
    print("this is calling apply twice ", x)
    return func(func(x))


def add_one(n):
    print("this is calling add_one", n)
    return n + 1


print(apply_twice(add_one, 5))  # """
"""
1. What is a Function?

A function is a block of reusable code that performs a specific task.

Helps make code modular, reusable, and readable.

Syntax:
"""

"""
def function_name(num):
    # code block
    for i in range(2, num):
        if num % i == 0:
            result= "this is not prime"
            break
    else:
        result= "this is  prime"
    return result

print(function_name(7))
print(function_name(8))
"""

"""
A. Positional Arguments

Passed in the correct order.
"""


def add(a, b, c):
    return a + b + c


print(add(5, 3, 6))  # 8


# without args
def without_args():
    return "this is without args function"


print(without_args())  # 8

"""
c. Keyword Arguments

Passed by name, order doesn’t matter.
"""


def introduce(name, age):
    print(f"My name is {name}, and I am {age} years old.")


introduce(age=25, name="Alice")

"""
c. default Arguments

"""


def introduce_default(name, age=25):
    print(f"My name is {name}, and I am {age} years old.")


introduce_default("Alice")

"""
D. Variable-Length Arguments – *args

Allows passing multiple positional arguments.

Inside the function, they are stored as a tuple.

"""


def add_all(*args):
    print("this is *args", args)
    return sum(args)


print(add_all(2, 4, 6))  # 12
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all(10, 10, 20, 40, 70, 90, 1000))

"""
E. Variable-Length Keyword Arguments – **kwargs

Allows passing multiple keyword arguments.

Inside the function, they are stored as a dictionary.
"""


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


student_info(name="Alice", age=22, course="Python")
student_info(name="Alice", age=22, course="Python", city="Doha")

"""
F. Mixing Arguments

Order must be:
positional → *args → default → **kwargs
"""


def mixup_fuc(name, age, **kwargs):
    print(f"may name is {name} and age {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


mixup_fuc("shyamji", 30, city="Doha", course="Python", country="Qatar")


def mixup_fuc(*args,  **kwargs):
    print(f"may name is {args}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


mixup_fuc("shyamji", 30, city="Doha", course="Python", country="Qatar")

"""
g. Recursive Functions

A function that calls itself.
5 -> 5*4*3*2*1 = 120
"""


def factorial(n):
    if n==0:
        return 1
    return n * factorial(n - 1)
    '''
    5* 4* 3* 2* 1 * 1
    '''

print(factorial(5))  # 120

"""

g. Lambda (Anonymous) Functions

Functions without a name.

Used for short, one-line operations.
"""


square = lambda x: x * x
# square = lambda 4: 4* 4
# lambda args: exp
print(square(4))  # 16

add = lambda a, b: a + b
print(add(3, 7))  # 10

# map(), filter(), sorted(), reduce -> pre defined fucntions
#map()

nums = [1, 2, 3, 4]
squares = list( map(lambda x: x*2, nums))
print(squares)  # [1, 4, 9, 16]

# without lambda
def multiply_num(num):
    l = []
    for x in nums:
        l.append(x*2)
    return l
print(multiply_num(nums))

# second exm with sort

students = [("Alice", 22), ("Bob", 19), ("Charlie", 25)]
students_sorted = sorted(students, key=lambda x: x[1])
# students_sorted = sorted(students, key=lambda x:x[1]) # ("Alice", 22)
print(students_sorted)  # [('Bob', 19), ('Alice', 22), ('Charlie', 25)]




