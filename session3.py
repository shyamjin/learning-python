"""
What is filter()?

filter() takes two arguments: a function and an iterable.

It filters out elements of the iterable for which the function returns False.

Returns a filter object, which can be converted to a list.
"""

nums = [2,4,6,7]
evens = filter(lambda x :x%2==0, nums )
print(list(evens)) #[2,4,6]


"""
What is reduce()?

reduce() is used to reduce a sequence of values into a single value.

Takes two arguments: a function and an iterable. (list, tuple, set, dict)

The function must take two arguments.

In Python 3, reduce() is in functools.
"""
from functools import reduce
nums = [2,4,6,7]
result = reduce(lambda x,y:x*y, nums)
print(result)
