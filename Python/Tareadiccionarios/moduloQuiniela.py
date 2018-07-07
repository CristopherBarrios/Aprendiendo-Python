#cristopher jose rodolfo barrios solis
#18207

def ingresar(orden,nombre,lista):#se utiliza el nombre orden y lista
    try:
       respuesta=lista[orden]=[nombre]+lista[orden]#ingresando cada operacion
    except KeyError:#si tira un error ingresar uno nuevo
        respuesta = lista[orden]=[nombre]
        return respuesta
    return respuesta
def eliminar(lista,orden):
    del lista[orden]#utilizando del para eliminar
def eliminar_apuesta(lista,orden,nombre):
    lista[orden].remove(nombre)
    cantidad = len(lista[orden])
    if cantidad == 0:#si no hay nadie borrar el equipo
        del lista[orden]
def mostar(lista,orden):#encontrando valor especifico
    try:
        respuesta =lista[orden]#mostrar el nombre
    except KeyError:
        respuesta = "No hay aficionados en el equipo"#mensaje si no hay
        return respuesta
    return respuesta
