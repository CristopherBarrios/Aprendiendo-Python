#cristopher jose rodolfo barrios solis
#18207

from moduloinsectos import ingresar, eliminar, mostar#importando el modulo

#utilizando la lista para usarla
insectos = {"lepidopteros": "mariposas", "odonatos": "libelulas", "coleopteos": "escarabajos", "ortopteros": "saltamontes", "dipteros": "moscas"}
preguntaOrden = str(input("Ingrese el orden"))#preguntando orden
preguntaNombre = str(input("ingrese nombre comun"))#preguntando nombre
ingresados = ingresar(preguntaOrden, preguntaNombre,insectos)#utilizando la guncion
print(insectos)
eliminarOrden = str(input("ingrese orden para eliminar"))
eliminando = eliminar(insectos, eliminarOrden)#utilizando la funcion
preguntamost = str(input("ingrese orden a mostrar"))
observar = mostar(insectos, preguntamost)#utilizando la guncion
print(observar)
for i in insectos:#ciclo for para mostrar todos los datos
    print("los " + i + " son " + insectos[i])


