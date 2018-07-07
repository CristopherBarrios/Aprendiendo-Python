#cristopher jose rodolfo barrios solis
#18207

def descifrar(num):#funcion para descifar el mensaje
    num = str(num)#convirtiendo a string
    with open(num) as archivo:
        linea = archivo.read()
        otro = linea[::-1]#invierte el texto
        nuevo = open("respuesta.txt","w")
        nuevo.write(str(otro)+"\n")#escribe en texto
        nuevo.close()#cierra el archivo
        return nuevo
