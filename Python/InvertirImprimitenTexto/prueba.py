
from moduloIO import leerArchivo#importarndo modulos
from descifrador import descifrar
pregunta = str(input("ingrese archivo: "))
contenido = leerArchivo(pregunta)#usarndo la funcion
contenido2 = descifrar(pregunta)
print(contenido)#imprimiendo el mensaje
print("decriptando el archivo mensaje.txt\n\n""el mensaje es:\n\n",contenido2)
