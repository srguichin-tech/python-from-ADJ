Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #ciclos en python if : IF significa si, y en programacion se usa para tomar desiciones. Sirve para decirle Python '\si pasa esto, has esto
>>> ejemplo 1
  File "<python-input-1>", line 1
    ejemplo 1
            ^
SyntaxError: invalid syntax
>>> x=10
>>> si x>5:
  File "<python-input-3>", line 1
    si x>5:
       ^
SyntaxError: invalid syntax
>>> si x > 5 :
  File "<python-input-4>", line 1
    si x > 5 :
       ^
SyntaxError: invalid syntax
>>> if x > 5 :
...     print('el numero es mayo que 5')
...
el numero es mayo que 5
>>> #como funciona if en pasos, python lee la condicion de esta en if . Si la condicion es verdade executa el comando
>>> # añadiendo else 'si no'
>>> x=2
>>> if x > 5 :
...     print ('el numero es mayor que 5')
... else:
...     print ('el numero es menor o igual a 5')
...
...
el numero es menor o igual a 5
>>> # ahora utilizando elif
>>> x = 8
>>> if x > 5:
...     print('mayor que 5')
... else x==5:
...     print('igual a 5')
... else :
...     print ('menor que 5')
...
  File "<python-input-12>", line 3
    else x==5:
         ^
SyntaxError: expected ':'
>>> if x > 5:
...     print('mayor que 5')
... else x == 5:
...     print('igual a 5')
... else :
...     print ('menor que 5')
...
  File "<python-input-13>", line 3
    else x == 5:
         ^
SyntaxError: expected ':'
>>> if x > 5:
...     print('mayor que 5')
... elif x == 5:
...     print('igual a 5')
... else :
...     print ('menor que 5')
...
mayor que 5
>>>
