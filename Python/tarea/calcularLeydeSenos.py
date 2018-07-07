#menuFunciones.py
# miercoles 7 de mar del 2018
#cristopher jose rodolfo barrios solis
#18207
#ejercicio 1

from funcionesUtiles import sacar_lado, sacar_angulo, validarNumero, math#se importan las funciones del modulo

ciclo = input("***************Calculadora de ley de senos**************\n"
                              "a/sen(alpha)=b/sen(beta))                \n"
              "*********************************************************\n\n"
              "1. calcular lado para dos angulos y un lado\n"
              "2. calcular angulo para dos lados y un angulo\n"
              "3. salir\n"
              "Ingrese una opcion: ")#pregunta de centinela
validar = validarNumero(ciclo)#utilizando la funcion para que solo acepte numeros
if validar=="True":
    while (ciclo!="3"):#centinela
        #condicion para encontrar el lado con seno
        if ciclo=="1":
            alpha= input("\n""ingresar el valor del angulo alpha: ")
            validarAlpha = validarNumero(alpha)#utilizando la funcion para que solo acepte numeros
            if validarAlpha=="True":
                beta = input("Ingrese el valor del angulo beta: ")
                validarBeta = validarNumero(beta)#utilizando la funcion para que solo acepte numeros
                if validarBeta=="True":
                    pregunta= str(input("desea calcular el lado a o b?: "))
                    if pregunta=="a":
                        numeroA = input("ingrese el valor del lado b: ")
                        validarA = validarNumero(numeroA)#utilizando la funcion para que solo acepte numeros
                        if validarA=="True":
                            pregunta2=str(input("escriba 1 si desea el resultado en grados o 2 si lo desea en radianes: "))
                            if pregunta2=="1":
                                calcularA= math.degrees(sacar_lado(alpha,beta,numeroA))#utilizando la funcion de seno, y tambien degrees para encontrar la respuesta en grados
                                print(calcularA)
                            elif pregunta2=="2":
                                calcularA= sacar_lado(alpha,beta,numeroA)#utilizando la funcion de seno
                                print(calcularA)
                            else:
                                print("ingrese un valor correcto")
                        else:
                            print("ingrese un numero")
                    elif pregunta=="b":
                        numeroB = input("ingrese el valor del lado a: ")
                        validarB = validarNumero(numeroB)#utilizando la funcion para que solo acepte numeros
                        if validarB=="True":
                            pregunta2=str(input("escriba 1 si desea el resultado en grados o 2 si lo desea en radianes: "))
                            if pregunta2=="1":
                                calcularB= math.degrees(sacar_lado(beta,alpha,numeroB))#utilizando la funcion de seno, y tambien degrees para encontrar la respuesta en grados
                                print (calcularB)
                            elif pregunta2=="2":
                                calcularB= sacar_lado(beta,alpha,numeroB)#utilizando la funcion de seno
                                print(calcularB)
                            else:
                                print("ingrese un valor correcto")
                        else:
                            print("ingrese un numero")
                    else:
                        print("ingrese un valor premitido")
                        
                else:
                    print("ingrese un numero")
            else:
                print("ingrese un numero")
        #condicion para encontrar el angulo con seno
        elif ciclo=="2":
            alpha= input("\n""ingresar el valor del lado a: ")
            validarAlpha = validarNumero(alpha)#utilizando la funcion para que solo acepte numeros
            if validarAlpha=="True":
                beta = input("Ingrese el valor del lado b: ")
                validarBeta = validarNumero(beta)#utilizando la funcion para que solo acepte numeros
                if validarBeta=="True":
                    pregunta= str(input("desea calcular el angulo alpha o beta?: "))
                    if pregunta=="alpha":
                        numeroA = input("ingrese el valor del angulo beta: ")
                        validarA = validarNumero(numeroA)#utilizando la funcion para que solo acepte numeros
                        if validarA=="True":
                            pregunta2=str(input("escriba 1 si desea el resultado en grados o 2 si lo desea en radianes: "))
                            if pregunta2=="1":
                                calcularA= math.degrees(sacar_angulo(numeroA,alpha,beta))#utilizando la funcion de seno, y tambien degrees para encontrar la respuesta en grados
                                print(calcularA)
                            elif pregunta2=="2":
                                calcularA= sacar_angulo(numeroA,alpha,beta)#utilizando la funcion de seno
                                print(calcularA)
                            else:
                                print("ingrese un valor correcto")
                        else:
                            print("ingrese un numero")
                    elif pregunta=="beta":
                        numeroB = input("ingrese el valor del angulo alpha: ")
                        validarB = validarNumero(numeroB)#utilizando la funcion para que solo acepte numeros
                        if validarB=="True":
                            pregunta2=str(input("escriba 1 si desea el resultado en grados o 2 si lo desea en radianes: "))
                            if pregunta2=="1":
                                calcularB= math.degrees(sacar_angulo(numeroB,beta,alpha))#utilizando la funcion de seno, y tambien degrees para encontrar la respuesta en grados
                                print(calcularB)
                            elif pregunta2=="2":
                                calcularB= sacar_angulo(numeroB,beta,alpha)#utilizando la funcion de seno
                                print(calcularB)
                            else:
                                print("ingrese un valor correcto")
                        else:
                            print("ingrese un numero")
                    else:
                        print("ingrese un valor premitido")
                        
                else:
                    print("ingrese un numero")
        else:
            print("ingrese un numero de la lista")
        ciclo = input("\n\n""***************Calculadora de ley de senos**************\n"
                              "a/sen(alpha)=b/sen(beta))                \n"
              "*********************************************************\n\n"
              "1. calcular lado para dos angulos y un lado\n"
              "2. calcular angulo para dos lados y un angulo\n"
              "3. salir\n"
              "Ingrese una opcion: ")
else:
    print("ingresar un numero porfavor")
print("\n""Adios!")#despedida
