Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c=['amith']
>>> c
['amith']
>>> dir(c)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> c="python"
>>> c
'python'
>>> list(c)
['p', 'y', 't', 'h', 'o', 'n']
>>> d==list(c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d==list(c)
NameError: name 'd' is not defined
>>> d=list(c)
>>> d
['p', 'y', 't', 'h', 'o', 'n']
>>> d[1:4:1]
['y', 't', 'h']
>>> pop(c,5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pop(c,5)
NameError: name 'pop' is not defined
>>> d.pop
<built-in method pop of list object at 0x000002A48AB73E00>
>>> d.pop()
'n'
>>> d
['p', 'y', 't', 'h', 'o']
>>> e= " class"
>>> e
' class'
>>> e=list(e)
>>> e
[' ', 'c', 'l', 'a', 's', 's']
>>> d+e
['p', 'y', 't', 'h', 'o', ' ', 'c', 'l', 'a', 's', 's']
>>> a=30
>>> b=7
>>> a
30
>>> b
7
>>> a/b
4.285714285714286
>>> a%b
2
>>> a//b
4
>>> 'a=',b
('a=', 7)
>>> 'b=',a
('b=', 30)
>>> a
30
>>> a
30
>>> b
7
>>> 'a=' ,a
('a=', 30)
>>> a,b=b,a
>>> a
7
>>> b
30
>>> x=5
>>> y=12
>>> temp=x
>>> x=y
>>> y=temp
>>> x
12
>>> y
5
>>> x
12
>>> y
5
>>> x=x^y
>>> y=x^y
>>> x=v^y
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x=v^y
NameError: name 'v' is not defined
>>> x=x^y
>>> x
5
>>> y
12
>>> 
>>> 
>>> x
5
>>> y
12
>>> x=x+y
>>> y=x-y

>>> x=x-y
>>> x
12
>>> y
5
>>> x
12
>>> dir(x)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> x
12
>>> y
5
>>> x=x*y
>>> y=x/y
>>> x=x/y
>>> x
5.0
>>> y
12.0
>>> x=(x&y) + (x|y)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    x=(x&y) + (x|y)
TypeError: unsupported operand type(s) for &: 'float' and 'float'
>>> a=10
>>> b=90
>>> a
10
>>> b
90
>>> a=(a&b)+(a|b)
>>> b=a+(~b)+1
>>> a=a+(~b)+1
>>> a
90
>>> b
10
>>> c="Extensive knowledge as a systems architect and software developer – analysis, development and management of complex software solutions."
>>> dir(c)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(c.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> c.count()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    c.count()
TypeError: count() takes at least 1 argument (0 given)
>>> c.cout(substring,string=Extensive knowledge as a systems architect and software developer – analysis, development and management of complex software solutions..end=.)
SyntaxError: invalid syntax
>>> c.cout()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    c.cout()
AttributeError: 'str' object has no attribute 'cout'
>>> c.split()
['Extensive', 'knowledge', 'as', 'a', 'systems', 'architect', 'and', 'software', 'developer', '–', 'analysis,', 'development', 'and', 'management', 'of', 'complex', 'software', 'solutions.']
>>> len(c.split())
18
>>> h=9900662117
>>> print("ur phone num is")
ur phone num is
>>> print("ur phone num is"h())
SyntaxError: invalid syntax
>>> print("ur phone num is")
ur phone num is
>>> print("ur phone num is"h)
SyntaxError: invalid syntax
>>> print("ur phone num is=",h)
ur phone num is= 9900662117
>>> print("ur phone num is=",h,"=+91")
ur phone num is= 9900662117 =+91
>>> print("ur phone num is=",h"=+91",)
SyntaxError: invalid syntax
>>> print("ur phone num is=+91",h)
ur phone num is=+91 9900662117
>>> h
9900662117
>>> print("ur phone num is=+91",h)
ur phone num is=+91 9900662117
>>> h
9900662117
>>> if(len(h)>0)
SyntaxError: invalid syntax
>>> h
9900662117
>>> if(len(h)>10)
SyntaxError: invalid syntax
>>> h
9900662117
>>> 
>>> 
>>> 
>>> h="9900662117"
>>> h1="+91"
>>> h1="+919900662117"
>>> h[-10:]
'9900662117'
>>> h1[-10:]
'9900662117'
>>> print("ur phone num is=+91",h[-10:])
ur phone num is=+91 9900662117
>>> print("ur phone num is=+91",h1[-10:])
ur phone num is=+91 9900662117
>>> 