#cristopherr jose rodolfo barrios solis
#18207

from moduloQuiniela import ingresar, eliminar, mostar, eliminar_apuesta#uso del modulo

quiniela = {
    'Argentina' : ['Luis','Adriana','Leslie'],
    'Alemania' : ['Pedro', 'Helena', 'Maria', 'Pablo'],
    'Brasil' : ['Marlene', 'Ricardo']#diccionario de quiniela
    }
print("Bienvenido a la quiniela del mundial!\n")
preguntaCT = str(input("1. Ingresar apuesta\n"
                       "2. Desplegar todas las apuestas\n"
                       "3. Desplegar lista de aficionados por equipo\n"
                       "4. Eliminar pais de la quiniela\n"
                       "5. Eliminar apuesta de persona\n"
                       "6. Salir\n"
                       "Ingrese el numero de lo que desea hacer: "))#pregunta para el centinela

while(preguntaCT != "6"):#ciclo para poder usar el menu
    if preguntaCT == "1":#ingresar apuesta
        preguntaPais = str(input("ingrese el pais que desea apostar: "))
        preguntaNombre = str(input("ingrese su nombre: "))
        apuesta = ingresar(preguntaPais, preguntaNombre, quiniela)
    elif preguntaCT == "2":#desplegar todas las apuestas
        for i in quiniela:
            print ("Para",i,"apuestan:",quiniela[i])
    elif preguntaCT == "3":#muestra
        preguntaMostrar = str(input("Ingrese equipo para desplegar a todos los aficionados: "))
        mostrando = mostar(quiniela,preguntaMostrar)
        print (mostrando)
    elif preguntaCT == "4": #eliminar apuesta de persona
        eliminarPais = str(input("Ingrese el equipo que desea eliminar: "))
        eliminandoPais = eliminar(quiniela, eliminarPais)
    elif preguntaCT == "5":#eliminar apuesta de persona
        eliminarAficionadoPais = str(input("Ingrese el pais del aficionado que desea eliminar: "))
        eliminarAficionado = str(input("Ingrese el aficionado que desea eliminar: "))
        eliminandoApuesta = eliminar_apuesta(quiniela,eliminarAficionadoPais,eliminarAficionado)
    else:
        print("\n\n""El comando no existe")
    preguntaCT = str(input("\n\n""1. Ingresar apuesta\n"
                       "2. Desplegar todas las apuestas\n"
                       "3. Desplegar lista de aficionados por equipo\n"
                       "4. Eliminar pais de la quiniela\n"
                       "5. Eliminar apuesta de persona\n"
                       "6. Salir\n"
                       "Ingrese el numero de lo que desea hacer: "))







