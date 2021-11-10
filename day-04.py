Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=zero(10)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=zero(10)
NameError: name 'zero' is not defined
>>> a=0**10
>>> a
0
>>> a=0*10
>>> a
0
>>> a=10*0
>>> a
0
>>> n=0
>>> for x in range(10)
SyntaxError: invalid syntax
>>> for x in range(n)
SyntaxError: invalid syntax
>>> n
0
>>> n=[0,0,0,0,0,0,0,0,0,0]
>>> n
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> n=0
>>> n*10
0
>>> a=9
>>> a*2
18
>>> n=0
>>> n**10
0
>>> n
0
>>> c=[0]*10
>>> c
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> a="manaswini"
>>> print('the sting is',a)
the sting is manaswini
>>> print('length of string is' len(a))
SyntaxError: invalid syntax
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> length(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    length(a)
NameError: name 'length' is not defined
>>> len(a)
9
>>> n='12345688'
>>> help(n.zfill)
Help on built-in function zfill:

zfill(width, /) method of builtins.str instance
    Pad a numeric string with zeros on the left, to fill a field of the given width.
    
    The string is never truncated.

>>> m=n.zfill(10)
>>> n
'12345688'
>>> m
'0012345688'
>>> c=' manaswini'
>>> d='manasv '
>>> e=' manasv '
>>> help(c.strip)
Help on built-in function strip:

strip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading and trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.

>>> c
' manaswini'
>>> m=c.strip()
>>> m
'manaswini'
>>> n=d.strip()
>>> n
'manasv'
>>> o=e.strip()
>>> o
'manasv'
>>> c
' manaswini'
>>> m
'manaswini'
>>> help(m.ljust)
Help on built-in function ljust:

ljust(width, fillchar=' ', /) method of builtins.str instance
    Return a left-justified string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> m
'manaswini'
>>> m.ljust(20," ")
'manaswini           '
>>> m.rjust(20," ")
'           manaswini'
>>> m.rljust(20," ")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    m.rljust(20," ")
AttributeError: 'str' object has no attribute 'rljust'
>>> m.ljust(20," ") rjust(20," ")
SyntaxError: invalid syntax
>>> m.center(20)
'     manaswini      '
>>> r='to notice something that is partly hidden or not clear, or to discover something, especially using a special method'
>>> help(r.join)
Help on built-in function join:

join(iterable, /) method of builtins.str instance
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

>>> r
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method'
>>> r.replace(" ","")
'tonoticesomethingthatispartlyhiddenornotclear,ortodiscoversomething,especiallyusingaspecialmethod'
>>> r.replace(" ","_")
'to_notice_something_that_is_partly_hidden_or_not_clear,_or_to_discover_something,_especially_using_a_special_method'
>>> r.split()
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method']
>>> r
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method'
>>> i=r.split()
>>> i
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method']
>>> dir(i)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> print(listToString(i))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(listToString(i))
NameError: name 'listToString' is not defined
>>> i
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method']
>>> i.join()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    i.join()
AttributeError: 'list' object has no attribute 'join'
>>> ' '.join(i)
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method'
>>> o='manu'
>>> l=' 'join.(i,o)
SyntaxError: invalid syntax
>>> l=' '.join(i,o)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    l=' '.join(i,o)
TypeError: join() takes exactly one argument (2 given)
>>> i+o
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    i+o
TypeError: can only concatenate list (not "str") to list
>>> u=list(o)
>>> u
['m', 'a', 'n', 'u']
>>> i+u
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method', 'm', 'a', 'n', 'u']
>>> x=i+u
>>> x
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method', 'm', 'a', 'n', 'u']
>>> ' '.join(x)
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method m a n u'
>>> r.replace(" ","")
'tonoticesomethingthatispartlyhiddenornotclear,ortodiscoversomething,especiallyusingaspecialmethod'
>>> x.replace(" ","")
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    x.replace(" ","")
AttributeError: 'list' object has no attribute 'replace'
>>> x
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method', 'm', 'a', 'n', 'u']
>>> ' '.join(x)
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method m a n u'
>>> x.replace(" ","")
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    x.replace(" ","")
AttributeError: 'list' object has no attribute 'replace'
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> type(x)
<class 'list'>
>>> ' '.join(x)
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method m a n u'
>>> type(x)
<class 'list'>
>>> r
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method'
>>> x
['to', 'notice', 'something', 'that', 'is', 'partly', 'hidden', 'or', 'not', 'clear,', 'or', 'to', 'discover', 'something,', 'especially', 'using', 'a', 'special', 'method', 'm', 'a', 'n', 'u']
>>> m=' '.join(i)
>>> m
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method'
>>> o
'manu'
>>> m+o
'to notice something that is partly hidden or not clear, or to discover something, especially using a special methodmanu'
>>> m+" "o
SyntaxError: invalid syntax
>>> o
'manu'
>>> o=" manu"
>>> o
' manu'
>>> m+o
'to notice something that is partly hidden or not clear, or to discover something, especially using a special method manu'
>>> type(m)
<class 'str'>
>>> type(o)
<class 'str'>
>>> type(x)
<class 'list'>
>>> 