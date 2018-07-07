#cristopher jose rodolfo barrios solis
#18207


preguntaNombre = input("Ingrese su nombre solo se admiten 20 caracteres: ")#pregunta inicial
caracteres = len(preguntaNombre)#cuantos caracteres ingreso el usuario
numeros = preguntaNombre.isnumeric()#verifica si es numerico el valor ingresado
if numeros == False:#si es falso significa que solo tiene letras
    if caracteres <= 20:#acepta solo 20 caracteres
        preguntaCorreo = input("Ingrese su correo: ")
        numerosCorreo = preguntaCorreo.isnumeric()#verifica si es numerico el valor ingresado
        if numerosCorreo== False:
            arrova = preguntaCorreo.find('@')
            if arrova != -1:#si no tiene arrova devuelve -1
                subcadena = preguntaCorreo[arrova -arrova: +arrova]#tiene escrito solo lo anterior a la arrova
                sitio = preguntaCorreo.find('.edu.gt')
                if sitio != -1:
                    subsubcadena = preguntaCorreo[sitio -sitio +arrova +1: +sitio]#usa solo lo que esta entre la arrova y .edu.gt
                    preguntaAsunto = input("ingrese su asunto: ")
                    numerosAsunto = preguntaAsunto.isnumeric()#verifica si es numerico el valor ingresado
                    if numerosAsunto ==False:
                        preguntaContenido = input("ingrese lo que quiera solicitar:\n")
                        numerosContenido =preguntaContenido.isnumeric()#verifica si es numerico el valor ingresado
                        if numerosContenido ==False:
                            caracteresContenido =len(preguntaContenido)#cuantos caracteres ingreso el usuario
                            if caracteresContenido <= 50:#acepta solo 50 caracteres
                                listas = [preguntaNombre,preguntaCorreo,preguntaAsunto,preguntaContenido," "]#concatenando todos los datos
                                archivo = open("archivo.txt","a")#crea archivo para escribir en el
                                for lista in listas:#utilizando las listas
                                    archivo.write(str(lista)+"\n")#escribiendo las listas
                                archivo.close()#cerrando el archivo
                                with open("archivo.txt") as archivo:#abriendo el archivo para leerlo
                                    linea = archivo.read()#leyendo el archivo
                                    print(linea)#mostrando lo leido
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
print("adios!")#despedida :)
