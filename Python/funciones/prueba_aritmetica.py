
from aritmetica import sumar, restar, multiplicar, dividir
a = input("ingrese numero a:\n")
b = input("ingrese numero b:\n")
a = int(a)
b = int(b)
valor1 = sumar(a, b)
valor2 = restar(a, b)
valor3 = multiplicar(a, b)
valor4 = dividir(a, b)
print("suma:",valor1,"\n""resta:" ,valor2,"\n""multiplicacion:", valor3,"\n""divicion:", valor4)
