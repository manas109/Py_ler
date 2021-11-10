Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> a
5
>>> type(a)
<class 'int'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> help(a)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> b=3.8
>>> b
3.8
>>> type(b)
<class 'float'>
>>> dir(b)
['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> hepl(b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    hepl(b)
NameError: name 'hepl' is not defined
>>> help(b)

>>> c=2+3j
>>> c
(2+3j)
>>> type(c)
<class 'complex'>
>>> dir(c)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
>>> help(c)

>>> a=9
>>> b=7
>>> a+b
16
>>> a,b=9,7
>>> a+b
16
>>> a=6,b=90
SyntaxError: cannot assign to literal
>>> a-b
2
>>> a/b
1.2857142857142858
>>> a*b
63
>>> a%b
2
>>> a//b
1
>>> 2**8
256
>>> a**2
81
>>> 3**3
27
>>> 16/12
1.3333333333333333
>>> a%b
2
>>> a,b=2.3,6.7
>>> a,b
(2.3, 6.7)
>>> type(a,b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    type(a,b)
TypeError: type() takes 1 or 3 arguments
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> a+b
9.0
>>> a-b
-4.4
>>> a*b
15.409999999999998
>>> a/b
0.34328358208955223
>>> a%
SyntaxError: invalid syntax
>>> a%b
2.3
>>> a//b
0.0
>>> a/b
0.34328358208955223
>>> a//b
0.0
>>> a=2+3j
>>> b=3+5j
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'complex'>
>>> dir(a)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
>>> dir(b)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
>>> a+b
(5+8j)
>>> a-b
(-1-2j)
>>> a/b
(0.6176470588235294-0.02941176470588238j)
>>> a%b
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a%b
TypeError: can't mod complex numbers.
>>> b%a
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b%a
TypeError: can't mod complex numbers.
>>> a=9.1
>>> b7.1
SyntaxError: invalid syntax
>>> b=7.1
>>> a/b
1.2816901408450705
>>> 9.1%7.1
2.0
>>> a//b
1.0
>>> a=2
>>> b=3
>>> a**2+2a*b+b**2
SyntaxError: invalid syntax
>>> a**2+(2a*b)+b**2
SyntaxError: invalid syntax
>>> a**2+2*a*b+b**2
25
>>> a,b=4,9
>>> a**2+2*a*b+b**2
169
>>> (a+b)**2
169
>>> c=input("enter a num;")
enter a num;8
>>> c
'8'
>>> type(c)
<class 'str'>
>>> dir(c)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(c)
No Python documentation found for '8'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> c=int(c)
>>> c
8
>>> type(c)
<class 'int'>
>>> a,b=21,7
>>> a=input("enter 1St nun;")
enter 1St nun;12
>>> a=int (input("enter 1St nun;"))
enter 1St nun;21
>>> a
21
>>> a=int (input("enter 1St nun;"))
enter 1St nun;a
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a=int (input("enter 1St nun;"))
ValueError: invalid literal for int() with base 10: 'a'
>>> a=int(input("enter 1St nun;"))
enter 1St nun;4
>>> a
4
>>> a='manu'
>>> a
'manu'
>>> b=''manu''
SyntaxError: invalid syntax
>>> "manu"
'manu'
>>> c='''manu'''
>>> c
'manu'
>>> d="""manu"""
>>> d
'manu'
>>> a="this is manaswini's laptop"
>>> a
"this is manaswini's laptop"
>>> a="this is "manaswini's" laptop"
SyntaxError: invalid syntax
>>> a="""this is manu"""
>>> a
'this is manu'
>>> a="""this is "manaswini's" laptop"""
>>> a
'this is "manaswini\'s" laptop'
>>> print(a)
this is "manaswini's" laptop
>>> a,b='a','b'
>>> a
'a'
>>> b
'b'
>>> a+b
'ab'
>>> a-b
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a*2
'aa'
>>> a*b
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(a.capitalize)
Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> 