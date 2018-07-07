Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
<function sumar at 0x7ff56b8a8488>
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/funciones.py", line 9, in <module>
    print (resultado)
NameError: name 'resultado' is not defined
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/funciones.py", line 4, in <module>
    from aritmetica import sumar
ImportError: No module named 'aritmetica'
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/funciones.py", line 4, in <module>
    from funciones import sumar
  File "/home/cristopher/Documentos/2018/Progra/funciones/funciones.py", line 4, in <module>
    from funciones import sumar
ImportError: cannot import name 'sumar'
>>> 
=============================== RESTART: Shell ===============================
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/funciones.py ==
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/funciones.py", line 4, in <module>
    from aritmetica import sumar
ImportError: No module named 'aritmetica'
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py", line 2, in <module>
    from aritmetica import sumar
ImportError: No module named 'aritmetica'
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py", line 2, in <module>
    from aritmetica import sumar
  File "/home/cristopher/Documentos/2018/Progra/funciones/aritmetica.py", line 2
    resultado = num1 + num2
            ^
IndentationError: expected an indented block
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py", line 2, in <module>
    from aritmetica import sumar
  File "/home/cristopher/Documentos/2018/Progra/funciones/aritmetica.py", line 2
    resultado = num1 + num2
            ^
IndentationError: expected an indented block
>>> 
== RESTART: /home/cristopher/Documentos/2018/Progra/funciones/aritmetica.py ==
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
15
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a5
ingrese numero b5
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py", line 6, in <module>
    valor = restar(a, b)
NameError: name 'restar' is not defined
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a5
ingrese numero b5
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py", line 6, in <module>
    valor = restar(a, b)
  File "/home/cristopher/Documentos/2018/Progra/funciones/aritmetica.py", line 5, in restar
    resultado = num1-num2
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a5
ingrese numero b5
Traceback (most recent call last):
  File "/home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py", line 7, in <module>
    valor = restar(a, b)
  File "/home/cristopher/Documentos/2018/Progra/funciones/aritmetica.py", line 5, in restar
    resultado = num1-num2
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a5
ingrese numero b5
0
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a5
ingrese numero b5
10 0
>>> 
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a
 RESTART: /home/cristopher/Documentos/2018/Progra/funciones/prueba_aritmetica.py 
ingrese numero a:
5
ingrese numero b:
5
suma: 10 
resta: 0
>>> 
