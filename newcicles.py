>>> # 7-11-25
>>> # continuando con ciclos. Else.
>>> x = 10
>>> if x > 5 :
...     print ('Es mayor que 5')
...
Es mayor que 5
>>> # ¿ Como funciona ?
>>> # python lee la condición que está después de if.En este caso: x > 5 Si la condición es verdadera (True), ejecuta e\l bloque indentado. Si es falsa (False), no hace nada (o ejecuta un else si lo hay).
>>> # Si es falsa (False), no hace nada (o ejecuta un else si lo hay).
>>> # Añadiendo else
>>> x = 4
>>> if x > 8 :
...     print ('Es mayor que 8')
... else:
...     print ('No es mayor que 8')
...
...
No es mayor que 8
>>> # Como se lee : “Si x es mayor que 5, imprime ‘El número es mayor que 5’; si no, imprime ‘El número es menor o igua\l a 5’.”
>>> # Utilizando elif
>>> x = 5
>>> if x > 5 :
...     print ('Es mayor que 5 ')
... elif x == 5 :
...     print ('Es igual al numero')
... else :
...     print ('Menor que 5')
...
Es igual al numero
>>> # como se lee: “Si x es mayor que 5**, imprime ‘Mayor que 5’;
>>> #“Si x es mayor que 5**, imprime ‘Mayor que 5’;
>>> #si no, pero x es igual a 5, imprime ‘Igual a 5’;
>>> #de lo contrario, imprime ‘Menor que 5’.”
>>>
>>>
>>> # combinando ciclos, ahora usar for
>>> for i range (6):
  File "<python-input-29>", line 1
    for i range (6):
          ^^^^^
SyntaxError: invalid syntax
>>> for i in range (6):
...     if i == 3 :
...         print ('igual a 3')
...     else :
...         print ('i no es 3 es'i)
...
  File "<python-input-30>", line 5
    print ('i no es 3 es'i)
           ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> for i in range (6):
...     if i == 3 :
...         print ('igual a 3')
...     else :
...         print ('i no es 3 es',i)
...
i no es 3 es 0
i no es 3 es 1
i no es 3 es 2
igual a 3
i no es 3 es 4
i no es 3 es 5
>>> # se lee : “Para cada número i del 0 al 5:
>>> #si i es igual a 3, imprime ‘i es igual a 3’;
>>> # si no, imprime ‘i no es 3, es i’.”
>>>
>>> # Resumen rapido de codigos significados de bucles:
>>> # if : si (condicion verdadera)
>>> # elif : si no, pero si
>>> # else : si ninguna condicion se cumple
>>> # ': ' marca el inicio del bloque del codigo.
>>>
