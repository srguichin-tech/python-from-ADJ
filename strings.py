Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #3.1.2 text
>>> # Python can manipulate text (represented by type str, so-called “strings”) as well as numbers
>>> 'hello world'
'hello world'
>>> "hello world"
'hello world'
>>> 'doesen't'
  File "<python-input-4>", line 1
    'doesen't'
            ^
SyntaxError: unterminated t-string literal (detected at line 1)
>>> 'doesen\'t'
"doesen't"
>>> "Doesen't"
"Doesen't"
>>> s= 'hello. \ world'
<python-input-7>:1: SyntaxWarning: "\ " is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\ "? A raw string is also an option.
>>> print(s)
hello. \ world
>>> s= 'hello. \n world'
>>> print(s)
hello.
 world
>>>
