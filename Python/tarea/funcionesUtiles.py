#menuFunciones.py
# miercoles 7 de mar del 2018
#cristopher jose rodolfo barrios solis
#18207
#ejercicio 1

import math#importando el modulo de math para senos
def validarNumero(num):#funcion para que valide solo numeros enteros
    try:
       num = int(num)
       
    except ValueError:#si tira un error despliega false
        respuesta ="False"
        return respuesta
    respuesta = "True"
    return respuesta

def validarDivisionEntreCero(num1,num2):#condicion para que no divida entre cero
    try:
        x = num1 / num2
    except ZeroDivisionError:
        respuesta = "False"
        return respuesta
    respuesta = "True"
    return respuesta

def opcionEnRango(num1,num2,num3):#condicion para que solo acepte numeros dentro del rago que ingrese
    if (num1 >= num2 and num1<= num3):
        respuesta = "True"
        return respuesta
    else:
        respuesta ="False"
        return respuesta

def sacar_lado(alpha,beta,num):#ecuacion para encontrar el lado del triangulo con senos
    alpha = float(alpha)
    beta = float(beta)
    num= float(num)
    resultado= num*(math.sin(alpha) / math.sin(beta))
    return resultado

def sacar_angulo(alpha,num2,num3):#funcion para encontrar el angulo con senos
    alpha= float(alpha)
    num2= float(num2)
    num3= float(num3)
    angulo= math.sin(alpha)
    resultado= math.asin((angulo/num2)*num3)
    return resultado
