#conversiones.py
# miercoles 28 de febrero del 2018
#cristopher jose rodolfo barrios solis
#ejercicio de funciones

#variables de la ecuacion
a = 9/5
e = 5/9
c = 32
menu = input("que desea hacer?\n\n"
             "1. convertir de grados farenheit a centigrados\n"
             "2. convertir de grados centigrados a farenheit\n"
             "3. salir\n\n")#pregunta para el centinela
menu = str(menu)#valor de menu en string
while (menu!="3"):
    from conversiones import convertir_centigrados_farenheit, convertir_farenheit_centigrados#llamando las funciones
    if menu == "1":#condicion para farenheit para converit a centigrados
        d = input("\n""ingrese grados farenheit para convertir a centigrados:\n\n")
        d = int(d)
        valor = convertir_farenheit_centigrados(d,c,e)#uso de la funcion
        print ("\n",valor, "Celsius\n")
    if menu == "2":#condicion para convertir de centigrados a farentheit
        b = input("\n""ingrese grados centigrados para convertir a farenheit:\n\n")
        b = int(b)
        valor2 = convertir_centigrados_farenheit(a,b,c)#uso de la funcion
        print ("\n",valor2,"Farenheit\n")
    menu = input("\n""que desea hacer?\n\n"
             "1. convertir de grados farenheit a centigrados\n"
             "2. convertir de grados centigrados a farenheit\n"
             "3. salir\n\n")#pregunta final para el centinela
print("\n""adios")#el programa se despide
