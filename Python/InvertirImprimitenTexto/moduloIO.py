#cristopher jose rodolfo barrios solis
#18207

def leerArchivo(num):#funcion para imprimir el mensaje
    num = str(num)#convirtiendo a string
    with open(num) as archivo:
        linea = archivo.read()#leyendo el archivo
        return linea
