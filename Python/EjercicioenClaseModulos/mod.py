#convertir_numero_a_letra.py
# lunes 5 de mar del 2018
#cristopher jose rodolfo barrios solis
#18207
#Modulos

def sueldo_trabajadores(num1,num2,num3):
    igss = num1 * 0.0483
    iva = num1 * 0.12
    bono = num1 * (num2/100)
    aguinaldo = num1 * (num3/100)
    total = (bono+aguinaldo)-(bono+aguinaldo)
    return igss, iva, bono, aguinaldo, total
