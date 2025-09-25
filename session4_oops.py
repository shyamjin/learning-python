"""
1. Public variable/method
2. private variable/Method
3. protect variable/Method

"""
# Public varible
class Student:
    school_name = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
    def greet(self):
        print(f"hello my name is {self.name}")



s1 = Student("Alice")
print(s1.name)
s1.name ="Shyamji"
print(s1.name)
s1.greet()

# private varibale
"""
👉 Defined with two underscores (__) at the start.
👉 Cannot be accessed directly outside the class.
"""

class Student:
    def __init__(self, name, marks):
        self.__marks = marks   # private variable
        self.name= name  #public variable

    def get_marks(self):
        return self.__marks

s = Student("Alex", 90)
print("before change",s.get_marks())

s.__marks = 1000
print("after change", s.get_marks())

# protected
"""
Defined with a single underscore (_).
👉 It’s a convention: "don’t use this variable outside the class (or subclass)".
👉 But still accessible (not truly private).
"""
print("------------------------------------------------------------")
class StudentProtected:
    def __init__(self, name, marks):
        self._marks = marks   # protected variable
        self.name= name  #public variable

    def get_marks(self):
        return self._marks

s1 = StudentProtected("Alex", 90)
print(s1._marks)
print("before change",s1.get_marks())

s1._marks = 1000
print("after change", s1.get_marks())

#Encapsulation
"""
1. Encapsulation

👉 Wrapping data (variables) and methods (functions) into a single unit (class).
👉 It helps in data hiding (not exposing internal details directly).
"""

print("------------------------------------------------------------")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500

print("------------------------------------------------------------")
"""
1. Inheritance

👉 A child class can use features (methods/variables) of the parent class.
"""
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def welcome(self):
        print("Hello my child")

c = Child()
c.greet()    # Inherited from Parent
c.welcome()  # Defined in Child

"""
1. Overriding

👉 When a child class defines a method that already exists in the parent class, the child’s method replaces (overrides) the parent’s method.
"""
print("------------------------------------------------------------")

class Parent:
    def greet(self):
        print("Hello from Parent")

    def bye(self):
        print("say bye")

class Child(Parent):
    def greet(self):
        print("Hello my child")

c = Child()
c.greet()
c.bye()# Inherited from Parent
print("-----------------------------------------------------")

"""
Overloading (Not directly in Python, but can be simulated)

👉 Having multiple methods with the same name but different arguments.
👉 Python doesn’t support true overloading, but we can achieve it using default arguments or *args.
"""
class MathOps:
    def add(self, a, b=0, c=0):  # default values simulate overloading
        return a + b + c

m = MathOps()
print(m.add(5, 10))       # 15
print(m.add(5, 10, 20))   # 35

"""
Types of Inheritance

Single Inheritance → One parent, one child.
"""
print("-----------------------------------------------------")

class Parent:
    def greet(self):
        print("Hello from Parent")

    def bye(self):
        print("say bye")

class Child(Parent):
    def greet(self):
        print("Hello my child")
c = Child()
c.greet()

"""
2
Multiple Inheritance → Child inherits from multiple parents.
"""
print("-----------------------------------------------------")
class Father:
    def greet(self):
        print("Hello from Parent")
class Mother:
    def run(self):
        print("Hello from mother")

class Child(Parent, Mother):
    def welcom(self):
        print("Hello my child")
c = Child()
c.greet()
c.run()
c.welcom()

"""
Multilevel Inheritance → Parent → Child → Grandchild.
"""

print("-----------------------------------------------------")
class GrandFather:
    def greet(self):
        print("Hello from GrandFather")
class Father(GrandFather):
    def run(self):
        print("Hello from father")

class Child(Father):
    def welcom(self):
        print("Hello my child")
c = Child()
c.greet()
c.run()
"""
Hierarchical Inheritance → One parent, multiple children.
"""
print("-----------------------------------------------------")
class Father():
    def run(self):
        print("Hello from father")

class Child1(Father):
    def welcom1(self):
        print("Hello my child")

class Child2(Father):
    def welcom2(self):
        print("Hello my child")
c = Child1()
c.run()

c2 = Child2()
c2.run()

"""
Hybrid Inheritance → Combination of above types.
"""
class A: pass
class B(A): pass
class C(A): pass
class D(B, C):  # Hybrid
    pass

"""
5. Polymorphism (many forms)

👉 The same function/method can behave differently depending on the object.
"""


def add(self, a, b=0, c=0):  # default values simulate overloading
    return a + b + c

add(2,3)
add(2,3,4)


class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

# Polymorphism in action
for animal in [Dog(), Cat()]:
    animal.sound()   # Output: Bark, Meow

print("------------------------------------------------")
"""
4. Abstraction

👉 Hiding implementation details and showing only the important features.
👉 In Python, done using abc module (Abstract Base Class).
"""
from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def welcome(self):
        pass

class Child(Parent):
    def welcome(self):
        print("hllow from abstraction")

c= Child()
c.welcome()

