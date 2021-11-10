Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c=[1,2,3.4,89,'manu']
>>> type(c)
<class 'list'>
>>> dir(c)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(c.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> c.copy
<built-in method copy of list object at 0x000002245707B900>
>>> help(c.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> c.count
<built-in method count of list object at 0x000002245707B900>
>>> c.count()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> help(c.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> c
[1, 2, 3.4, 89, 'manu']
>>> c.count(1)
1
>>> c.count('ma')
0
>>> c.count('manu')
1
>>> help(pop)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    help(pop)
NameError: name 'pop' is not defined
>>> help(c.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

>>> c
[1, 2, 3.4, 89, 'manu']
>>> c.pop(index=-2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c.pop(index=-2)
TypeError: list.pop() takes no keyword arguments
>>> c.pop(-2)
89
>>> c
[1, 2, 3.4, 'manu']
>>> help(c.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> c
[1, 2, 3.4, 'manu']
>>> c.insert(1,11)
>>> c
[1, 11, 2, 3.4, 'manu']
>>> help(c.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.

>>> c
[1, 11, 2, 3.4, 'manu']
>>> c.reverse()
>>> c
['manu', 3.4, 2, 11, 1]
>>> help(c.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.

>>> c.append(1)
>>> c
['manu', 3.4, 2, 11, 1, 1]
>>> c
['manu', 3.4, 2, 11, 1, 1]
>>> c.insert(2,'abc')
>>> c
['manu', 3.4, 'abc', 2, 11, 1, 1]
>>> c.insert(7, '1,2,3')
>>> c
['manu', 3.4, 'abc', 2, 11, 1, 1, '1,2,3']
>>> help(c.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> c.extend(3.4)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    c.extend(3.4)
TypeError: 'float' object is not iterable
>>> c.extend(0)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c.extend(0)
TypeError: 'int' object is not iterable
>>> c.extend('manu')
>>> c
['manu', 3.4, 'abc', 2, 11, 1, 1, '1,2,3', 'm', 'a', 'n', 'u']
>>> c.extend([1,2,3])
>>> c
['manu', 3.4, 'abc', 2, 11, 1, 1, '1,2,3', 'm', 'a', 'n', 'u', 1, 2, 3]
>>> 