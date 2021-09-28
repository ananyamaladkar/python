
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> i=10
>>> type (i)
<class 'int'>
>>> i=10.5
>>> type (i)
<class 'float'>
>>> height=1.75
>>> weight=65.4
>>> height
1.75
>>> weight
65.4
>>> bmi=weight/height**2
>>> bmi
21.355102040816327
>>> type(bmi)
<class 'float'>
>>> 10/5
2.0
>>> 5%3
2
>>> 2**5
32
>>> 5//2
2
>>> 5==5
True
>>> 5==3
False
>>>  5=!3
  File "<stdin>", line 1
    5=!3
IndentationError: unexpected indent
>>> 5!=3
True
>>>
>>> 6<4
False
>>>
>>> 'hello' < 'abc'
False
>>> 'hello' < 7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 'hello' < '7'
False