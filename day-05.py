Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={'name':'manu','num':9900}
>>> d
{'name': 'manu', 'num': 9900}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> from icecream imprt ic
SyntaxError: invalid syntax
>>> from icecream ic
SyntaxError: invalid syntax
>>> 
>>> from icecream as ic
SyntaxError: invalid syntax
>>> from icecream ic
SyntaxError: invalid syntax
>>> from icecream import ic
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    from icecream import ic
ModuleNotFoundError: No module named 'icecream'
>>> from icecream import ic
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    from icecream import ic
ModuleNotFoundError: No module named 'icecream'
>>> help(d.clear)
Help on built-in function clear:

clear(...) method of builtins.dict instance
    D.clear() -> None.  Remove all items from D.

>>> help(d.copy)
Help on built-in function copy:

copy(...) method of builtins.dict instance
    D.copy() -> a shallow copy of D

>>> d.copy()
{'name': 'manu', 'num': 9900}
>>> d.clear()
>>> d
{}
>>> d={'name': 'manu', 'num': 9900}
>>> help(d.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> d.fromkeys(d)
{'name': None, 'num': None}
>>> help(d.get)
Help on built-in function get:

get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.

>>> d.get()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 argument, got 0
>>> d.get(d)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.get(d)
TypeError: unhashable type: 'dict'
>>> x=d.get('people',7898)
>>> x
7898
>>> help(d.items)
Help on built-in function items:

items(...) method of builtins.dict instance
    D.items() -> a set-like object providing a view on D's items

>>> d.items()
dict_items([('name', 'manu'), ('num', 9900)])
>>> help(d.keys)
Help on built-in function keys:

keys(...) method of builtins.dict instance
    D.keys() -> a set-like object providing a view on D's keys

>>> d.keys()
dict_keys(['name', 'num'])
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(d.pop)
Help on built-in function pop:

pop(...) method of builtins.dict instance
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised

>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> 
>>> d
{'name': 'manu', 'num': 9900}
>>> d.pop(name)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d.pop(name)
NameError: name 'name' is not defined
>>> d.pop(name[manu])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.pop(name[manu])
NameError: name 'name' is not defined
>>> d.pop([manu])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    d.pop([manu])
NameError: name 'manu' is not defined
>>> help(d.popitem)
Help on built-in function popitem:

popitem() method of builtins.dict instance
    Remove and return a (key, value) pair as a 2-tuple.
    
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.

>>> d.popitem()
('num', 9900)
>>> help(d.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> d.setdefault(name)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d.setdefault(name)
NameError: name 'name' is not defined
>>> d.setdefault('name','anu')
'manu'
>>> d
{'name': 'manu'}
>>> x=setdefault("name","anu")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x=setdefault("name","anu")
NameError: name 'setdefault' is not defined
>>> d.setdefault("name", "anu")
'manu'
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(setdefault)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    help(setdefault)
NameError: name 'setdefault' is not defined
>>> help(d.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> help(d.update)
Help on built-in function update:

update(...) method of builtins.dict instance
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> d
{'name': 'manu'}
>>> d1={'mango': '2'}
>>> d.update(d1)
>>> d
{'name': 'manu', 'mango': '2'}
>>> help(d.values)
Help on built-in function values:

values(...) method of builtins.dict instance
    D.values() -> an object providing a view on D's values

>>> d.values()
dict_values(['manu', '2'])
>>> help(d.pop)
Help on built-in function pop:

pop(...) method of builtins.dict instance
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised

>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d
{'name': 'manu', 'mango': '2'}
>>> d.pop(2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d.pop(2)
KeyError: 2
>>> 
>>> d.pop(mango)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d.pop(mango)
NameError: name 'mango' is not defined
>>> d.pop('mango')
'2'
>>> d
{'name': 'manu'}
>>> help(d.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> d.fromkeys(d)
{'name': None}
>>> 
>>> 
>>> 
>>> s={1,1,2,3,3,7,4,99,99,0,11}
>>> type(s)
<class 'set'>
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> help(s.add)
Help on built-in function add:

add(...) method of builtins.set instance
    Add an element to a set.
    
    This has no effect if the element is already present.

>>> s.add(22)
>>> s
{0, 1, 2, 3, 4, 99, 7, 11, 22}
>>> s.clear()
>>> s
set()
>>> s={1,1,2,3,3,7,4,99,99,0,11}
>>> help(s.difference)
Help on built-in function difference:

difference(...) method of builtins.set instance
    Return the difference of two or more sets as a new set.
    
    (i.e. all elements that are in this set but not the others.)

>>> s1={1,2,33,4,456,677,8,09,11}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> s1={1,2,33,4,456,677,8,9,11}
>>> s1.difference()
{1, 2, 33, 4, 677, 456, 8, 9, 11}
>>> s.difference()
{0, 1, 2, 3, 4, 99, 7, 11}
>>> help(s.difference_update)
Help on built-in function difference_update:

difference_update(...) method of builtins.set instance
    Remove all elements of another set from this set.

>>> s1.difference_update()
>>> s1
{1, 2, 33, 4, 677, 456, 8, 9, 11}
>>> help(d.discard)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    help(d.discard)
AttributeError: 'dict' object has no attribute 'discard'
>>> help(s.discard)
Help on built-in function discard:

discard(...) method of builtins.set instance
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

>>> s.discard()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.discard()
TypeError: discard() takes exactly one argument (0 given)
>>> s
{0, 1, 2, 3, 4, 99, 7, 11}
>>> s.discard(99)
>>> s
{0, 1, 2, 3, 4, 7, 11}
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> help(s.intersection)
Help on built-in function intersection:

intersection(...) method of builtins.set instance
    Return the intersection of two sets as a new set.
    
    (i.e. all elements that are in both sets.)

>>> s.intersection(s1)
{1, 2, 11, 4}
>>> help(s.intersection_update)
Help on built-in function intersection_update:

intersection_update(...) method of builtins.set instance
    Update a set with the intersection of itself and another.

>>> s.intersection_update(s1)
>>> s
{1, 2, 11, 4}
>>> s1.intersection_update(s)
>>> s1
{1, 2, 11, 4}
>>> help(s.isdisjoint)
Help on built-in function isdisjoint:

isdisjoint(...) method of builtins.set instance
    Return True if two sets have a null intersection.

>>> s1.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    s1.isdisjoint()
TypeError: isdisjoint() takes exactly one argument (0 given)
>>> s.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s.isdisjoint()
TypeError: isdisjoint() takes exactly one argument (0 given)
>>> isdisjoint(s)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    isdisjoint(s)
NameError: name 'isdisjoint' is not defined
>>> s1.isdisjoint(s,s1)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s1.isdisjoint(s,s1)
TypeError: isdisjoint() takes exactly one argument (2 given)
>>> s1.isdisjoint(s)
False
>>> s.isdisjoint(s1)
False
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> help(s1.issubset)
Help on built-in function issubset:

issubset(...) method of builtins.set instance
    Report whether another set contains this set.

>>> s1.issubset(s)
True
>>> s.issubset(s1)
True
>>> help(s1.issuperset)
Help on built-in function issuperset:

issuperset(...) method of builtins.set instance
    Report whether this set contains another set.

>>> s.issuperset(s1)
True
>>> s1.issuperset(s)
True
>>> s
{1, 2, 11, 4}
>>> s1
{1, 2, 11, 4}
>>> help(s1.pop)
Help on built-in function pop:

pop(...) method of builtins.set instance
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

>>> s.pop(1)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    s.pop(1)
TypeError: pop() takes no arguments (1 given)
>>> s.pop()
1
>>> s
{2, 11, 4}
>>> s1
{1, 2, 11, 4}
>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> dir(s1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> help(s1.remove)
Help on built-in function remove:

remove(...) method of builtins.set instance
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.

>>> s.remove(11)
>>> s
{2, 4}
>>> s1
{1, 2, 11, 4}
>>> help(s1.symmetric_difference)
Help on built-in function symmetric_difference:

symmetric_difference(...) method of builtins.set instance
    Return the symmetric difference of two sets as a new set.
    
    (i.e. all elements that are in exactly one of the sets.)

>>> s.symmetric_difference(s1)
{1, 11}
>>> s1.symmetric_difference(s)
{1, 11}
>>> s
{2, 4}
>>> s1
{1, 2, 11, 4}
>>> s1.symmetric_difference_update(s)
>>> s
{2, 4}
>>> s1
{1, 11}
>>> help(s.symmetric_difference_update)
Help on built-in function symmetric_difference_update:

symmetric_difference_update(...) method of builtins.set instance
    Update a set with the symmetric difference of itself and another.

>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> help(s.union)
Help on built-in function union:

union(...) method of builtins.set instance
    Return the union of sets as a new set.
    
    (i.e. all elements that are in either set.)

>>> s1.union(s)
{1, 2, 11, 4}
>>> s
{2, 4}
>>> s1
{1, 11}
>>> help(s.update)
Help on built-in function update:

update(...) method of builtins.set instance
    Update a set with the union of itself and others.

>>> s.update()
>>> s
{2, 4}
>>> s1.update()
>>> s1
{1, 11}
>>> s.update(s1)
>>> s
{1, 2, 4, 11}
>>> s1
{1, 11}
>>> s1.update(s)
>>> s1
{1, 2, 4, 11}
>>> s
{1, 2, 4, 11}
>>> 