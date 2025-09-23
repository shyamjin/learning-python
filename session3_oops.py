"""
What is OOP?

Object-Oriented Programming is a programming paradigm that uses objects and classes.

Instead of writing everything as separate functions and variables, OOP organizes code around real-world entities.
Real-life analogy:

Class → Blueprint of a house

Object → Actual house built from the blueprint

# """
# nums = [1,2]
# nums2 = [2,3,4,5]
# def multiply_num(num):
#     l = [], s= []
#     for x in nums:
#         l.append(x*2)
#     for y in nums2:
#         s.apped(y)
#     return l, s
# print(multiply_num(nums))

class Person:
   def __init__(self):
       self.age=30 #variable
       print(self.age)
       self.name= "Shyamji"  #variable
       print(self.name)

   def greet(self): #method
       print(f"hellp my name is {self.name} and age is {self.age}")

obj = Person()
print(obj.name)
print(obj.age)
obj.greet()
"""
1. Instance Variables and Methods
Definition

Instance variables are unique to each object (each instance of a class).

Instance methods operate on instance variables and use self.
"""
class Person:
   def __init__(self):
       self.age=30 #instance variable
       print(self.age)
       self.name= "Shyamji"  #instance variable
       print(self.name)

   def greet(self): #instace method
       print(f"hellp my name is {self.name} and age is {self.age}")

obj = Person()
print(obj.name)
print(obj.age)

class Person2:
   def __init__(self, age, name):
       self.age=age #instance variable
       print(self.age)
       self.name= name  #instance variable
       print(self.name)

   def greet(self): #instace method
       print(f"hellp my name is {self.name} and age is {self.age}")

obj1 = Person2(30, "Alice")
print(obj1.name)
print(obj1.age)
obj12 = Person2(90, "John")
obj12.greet()
"""
2. Class Variables and Class Methods
Definition

Class variables are shared among all instances of a class.

Class methods operate on class variables and use @classmethod + cls instead of self.
"""


class Student:
    school_name = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
    def greet(self):
        print(f"hello my name is {self.name}")
        # print(f"hello my scheool is {self.school_name}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school_name)  # ABC School
s1.school_name ="testing"
print(s1.school_name)
print(s2.school_name)  # ABC School
s2.greet()
Student.change_school("abc")

# Change school using class method
# Student.change_school("XYZ School")
# print(s1.school_name)  # XYZ School
# print(s2.school_name)  # XYZ School

"""
3. Static Variables and Static Methods
Definition

Static variables are class-level variables often used inside static methods.

Static methods do not take self or cls, and are used as utility functions inside a class.
"""

class Calculator:
    def add(self,a, b): #instance metthod
        return a + b

obj3 = Calculator()
print(obj3.add(2,3))


def add(a, b):  # static metthod
    return a + b  #

class calc:
    @staticmethod
    def add( a, b):  # static metthod
        return a + b # static variable

print(calc.add(9,120))