#cristopher jose rodolfo barrios solis
#18207


suma = 0
cont=0# Iniciamos nuestros contadores o variables para sumar
dato = input("Ingrese un dato o escriba fin para terminar ") # Pedimos primer dato
while dato != "fin" and cont<100:
    cont = int(cont)+1# No se ha recibido la señal de fin de datos
    dato = int(dato)# Convertimos el dato para procesarlo
    suma = suma + dato # Acumulamos el valor leído al total.
    dato = input("Ingrese un dato o escriba fin para terminar")
print ("la suma es: ",suma)
print ("cantidad de edades leidas: ",cont)
promedio = suma/cont
print("promedio es: ", promedio)
