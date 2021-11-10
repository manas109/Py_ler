Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c='2'
>>> type(c)
<class 'str'>
>>> c=int(c)
>>> c
2
>>> type(c)
<class 'int'>
>>> dir(c)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> hepl(c.conjugate)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hepl(c.conjugate)
NameError: name 'hepl' is not defined
>>> help(c.conjugate)
Help on built-in function conjugate:

conjugate(...) method of builtins.int instance
    Returns self, the complex conjugate of any int.

>>> Returns self, the complex conjugate of any int.
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=[1,2.3,77,'manu',(5+7j)]
>>> a
[1, 2.3, 77, 'manu', (5+7j)]
>>> type(a)
<class 'list'>
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a.copy()
[1, 2.3, 77, 'manu', (5+7j)]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count(77)
1
>>> a.count(10)
0
>>> a.extend()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.extend()
TypeError: extend() takes exactly one argument (0 given)
>>> help(a.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> a.extend(22,5)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.extend(22,5)
TypeError: extend() takes exactly one argument (2 given)
>>> a.extend([22,5])
>>> a
[1, 2.3, 77, 'manu', (5+7j), 22, 5]
>>> help(a.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.list instance
    Return first index of value.
    
    Raises ValueError if the value is not present.

>>> a.extend([22])
>>> a
[1, 2.3, 77, 'manu', (5+7j), 22, 5, 22]
>>> a.index([22])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.index([22])
ValueError: [22] is not in list
>>> a
[1, 2.3, 77, 'manu', (5+7j), 22, 5, 22]
>>> element=77
>>> a.index(element)
2
>>> a.index((5+7j))
4
>>> help(a,insert)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    help(a,insert)
NameError: name 'insert' is not defined
>>> help(a.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> a.insert([99,2])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.insert([99,2])
TypeError: insert expected 2 arguments, got 1
>>> a.insert(99,2)
>>> a
[1, 2.3, 77, 'manu', (5+7j), 22, 5, 22, 2]
>>> a.insert(99,2)
>>> a
[1, 2.3, 77, 'manu', (5+7j), 22, 5, 22, 2, 2]
>>> a.insert(2,99)
>>> a
[1, 2.3, 99, 77, 'manu', (5+7j), 22, 5, 22, 2, 2]
>>> help(a.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> a
[1, 2.3, 99, 77, 'manu', (5+7j), 22, 5, 22, 2, 2]
>>> a.pop(-2)
2
>>> a
[1, 2.3, 99, 77, 'manu', (5+7j), 22, 5, 22, 2]
>>> help(a.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> a.remove(22)
>>> a
[1, 2.3, 99, 77, 'manu', (5+7j), 5, 22, 2]
>>> a.remove(22)
>>> a
[1, 2.3, 99, 77, 'manu', (5+7j), 5, 2]
>>> help(a.revers)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    help(a.revers)
AttributeError: 'list' object has no attribute 'revers'
>>> help(a.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> reverse(a)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    reverse(a)
NameError: name 'reverse' is not defined
>>> a.reverse()
>>> a
[2, 5, (5+7j), 'manu', 77, 99, 2.3, 1]
>>> help(a.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order.

>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'complex' and 'int'
>>> q=['q','e','p','i']
>>> q.sort()
>>> q
['e', 'i', 'p', 'q']
>>> 