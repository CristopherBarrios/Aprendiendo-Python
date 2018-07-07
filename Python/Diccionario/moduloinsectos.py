#cristopherr jose rodolfo barrios solis
#18207

def ingresar(orden,nombre,lista):#se utiliza el nombre orden y lista
    respuesta=lista[orden]=nombre#ingresando cada operacion
    return respuesta
def eliminar(lista,orden):
    del lista[orden]#utilizando del para eliminar

def mostar(lista,orden):#encontrando valor especifico
    respuesta =lista[orden]
    return respuesta
