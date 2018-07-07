#cristopher jose rodolfo barrios solis
#18207

from funcion import descifrar

preguntaNombre = input("Ingrese su nombre solo se admiten 20 caracteres: ")
caracteres = len(preguntaNombre)
numeros = preguntaNombre.isnumeric()
if numeros == False:
    if caracteres <= 20:
        preguntaCorreo = input("Ingrese su correo: ")
        numerosCorreo = preguntaCorreo.isnumeric()
        if numerosCorreo== False:
            arrova = preguntaCorreo.find('@')
            if arrova != -1:
                subcadena = preguntaCorreo[arrova -arrova: +arrova]
                sitio = preguntaCorreo.find('.edu.gt')
                if sitio != -1:
                    subsubcadena = preguntaCorreo[sitio -sitio +arrova +1: +sitio]
                    preguntaAsunto = input("ingrese su asunto: ")
                    numerosAsunto = preguntaAsunto.isnumeric()
                    if numerosAsunto ==False:
                        preguntaContenido = input("ingrese lo que quiera solicitar:\n")
                        numerosContenido =preguntaContenido.isnumeric()
                        if numerosContenido ==False:
                            caracteresContenido =len(preguntaContenido)
                            if caracteresContenido <= 50:
                                lista = [preguntaNombre,preguntaCorreo,preguntaAsunto,preguntaContenido]
                                print(lista)
                            else:
                                print("solo se permiten menos de 50 caracteres")
                        else:
                            print("no se permiten ingresar numeros")
                    else:
                        print("ingrese un valor correcto")
                else:
                    print("ingrese .edu.gt")
            else:
                print("ingrese la arrova")
    else:
        print("solo se permiten 20 caracteres")
else:
    print("ingrese datos validos")
print("adios")
