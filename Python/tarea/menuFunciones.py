#funcionesUtiles.py
# miercoles 7 de mar del 2018
#cristopher jose rodolfo barrios solis
#18207
#ejercicio 1

from funcionesUtiles  import validarNumero, validarDivisionEntreCero, opcionEnRango

numero = input("compruebe numero")
valor1 = validarNumero(numero)

print(valor1)


a = int(input("ingrese a"))
b = int(input("ingrese b"))

valor2 = validarDivisionEntreCero(a,b)

print(valor2)
x = int(input("ingreselo x"))
valor3 = opcionEnRango(x,a,b)
print (valor3)
