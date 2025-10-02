"""
Exception Handling  — Explained with Classes
"""

"""
try-except

👉 Use when you expect one common error and just want to handle it safely.
"""

#
# class ExceptionClass:
#     def handle_exception(self, a, b):
#         return a / b
#
#
# obj = ExceptionClass()
# # print(obj.handle_exception(4, 0))


class ExceptionClass:
    def handle_exception(self, a, b):
        try:
            return a / b
        except Exception as e:
            return f"Exception occurred due to {e}"


obj1 = ExceptionClass()
print(obj1.handle_exception(4, 0))
print('---------------------------------------')

"""Multi level exception"""
class CheckNum:
    def check_number(self, number):
        try:
            return int(number)
        except ValueError:
            return "wrong value"
        except TypeError:
            return "wrong type"


o = CheckNum()
print(o.check_number(9))
print(o.check_number("Shyamji")) #"wrong value"
print(o.check_number(None)) #"wrong type"
print("-----------------------------------------")
"""Multiple exception"""
class CheckNum:
    def check_number(self, number):
        try:
            return int(number)
        except (ValueError,TypeError):
            return "We found the exception into code.please check"

o1= CheckNum()
print(o1.check_number(None))

print("-----------------------------------------")
"""
 Using finally

👉 Use when you must run cleanup code, no matter what.
open the file, write file, db connection , loggging 
"""

class CheckNum:
    def check_number(self, number):
        try:
            return int(number)
        except (ValueError,TypeError):
            return "We found the exception into code.please check"
        finally:
            print("this is final block and doing some cleanup")

o1= CheckNum()
print(o1.check_number(None))

"""
print("-----------------------------------------")
5. Using else

👉 Use when you want code to run only if no error happens.
"""
print("-----------------------------------------")
class CheckNum:
    def check_number(self, number, number2):
        try:
            x= int(number)
            y = int(number2)
        except (ValueError,TypeError):
            return "We found the exception into code.please check"
        else:
            return f"this is else block and we don't have any exeption {x} {y}"
        finally:
            print("this is final block and doing some cleanup")


o2= CheckNum()
print(o2.check_number(2.8, 'shyamji'))

"""
print("-----------------------------------------")
5. Custom Exception

Custom exception 
"""
print("-----------------------------------------")

class NegativeNumberExpetionHandling(Exception):
    pass
class SquareRoot:
    def compute(self, n):
        if n < 0:
            raise NegativeNumberExpetionHandling("Negative numbers not allowed")
        return n ** 0.5

c= SquareRoot()
print(c.compute(2))
print("-----------------------------------------")
"""
if else with exception handling
"""
class CheckNum:
    def check_number(self, number, number2):
        try:
            x= int(number)
            y = int(number2)
            if x%y ==0:
                print("number is divisible")
            else:
                print("number is not divisible")

        except (ValueError,TypeError):
            return "We found the exception into code.please check"
        else:
            return f"this is else block and we don't have any exeption {x} {y}"
        finally:
            print("this is final block and doing some cleanup")

d= CheckNum()
print(d.check_number(4,None))