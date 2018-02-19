#cristopher jose rodolfo barrios solis
#18207

#preguntando que valores quiere el usuario, inicio, final, step
preguntaInicio = input("Este prorama solicita que usted indique el valor de inicio, fin y cada cuanto debe ganarse un valor\n""ingrese valor de inicio:\n")
preguntaFinal = input("ingrese valor final:\n")
preguntaRango = input("ingrese cada cuanto generar un valor:\n")

#convirtiendo las variables en int
preguntaInicio=int(preguntaInicio)
preguntaFinal=int(preguntaFinal)
preguntaRango=int(preguntaRango)

lista = range(preguntaInicio,preguntaFinal,preguntaRango)#poniendo las varibles en el range

#ciclo for para mostrar los numeros
for multiplo in lista:
    if(multiplo%4)== 0:#condicion numeros divisibles entre 4
        print (multiplo,"es divisible entre 4")
    else:
        print(multiplo,"no es divisible entre 4")
    if(multiplo%3)==0:#condicion de numeros divisibles entre 3
        print(multiplo,"es divisible entre 3")
    else:
        print(multiplo,"no es divisible entre 3")
    
