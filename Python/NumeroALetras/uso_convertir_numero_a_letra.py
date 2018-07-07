#convertir_numero_a_letra.py
# lunes 5 de mar del 2018
#cristopher jose rodolfo barrios solis
#18207
#tarea

from convertir_numero_a_letra import convertir#manda a llamar la funcion
a = input("Hola\n"
          "En en este programa te pregunta que numero ingreses y te lo convierte en numeros\n"
          "Escribe en el rango 0-100 o escribe fin para seguir con la siguiente pregunta\n\n\n"
          "Escribe un numero o fin:\n")#pregunta del centinela
while(a!="fin"):#centinela
    a = int(a)#convierte en entero la respuesta
    valor1 = convertir(a)#metiendo el numero en la funcion en una variable
    print (valor1,"\n")#mostrandoel resultado
    a = input("Escribe un numero o fin:\n")#pregunta del centinela
b = input("Desea mostrar todos los numero del 0 al 100 en letras?\n"
          "si o no:\n")#pregunta del rango
b = str(b)#convirtiendo en valor string
if b=="si":#condicion 
    for valor1 in range(0,101):#ciclo for para mostrarlo todo en ese rango
        valor2 = convertir(valor1)#metiendo los numeros de for en la funcion
        print (valor1, valor2)#mostrando todo el ciclo
else:
    print("Adios!")#despedida jeje
