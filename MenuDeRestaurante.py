#cristopher jose rodolfo barrios solis
#18207

#menu del restaurante
combo = input("*******************************************************\n"
                          "            BIENVENIDO AL RESTAURANTE\n"
                          "*******************************************************\n"
                          "COMBO 1: 3 tacos al pastor y 1 bebida............Q15.00\n"
                          "COMBO 2: 3 tacos de cochinita pibil y 1 bebida...Q18.00\n"
                          "COMBO 3: 2 gringas al pastor y 1 bebida..........Q25.00\n\n"
                          "Acciones que puede ejecutar:\n"
                          "- Indicar el numero del combo que desea.\n"
                          "- Ingresar 'Solamente eso' para indicar que ya termino de ordenar.\n"
                          "- Ingresar 'Modificar' si desea eliminar un item de su orden.\n")
#iniciando las variables
suma=0
suma1=0
suma2=0
suma3=0
while(combo !="Solamente eso"):#centinela para que terminar el pedido
    combo=str(combo)

    #condicion para que solo acepte los valores 1, 2, 3, solamente eso, modificar
    if combo=="1" or combo=="2" or combo=="3" or combo=="Solamente eso" or combo=="Modificar":
        
        if combo=="Modificar":#condicion para que cuando escriba modificar pueda eliminar una opcion
            
            pregunta = input("ingrese numero de combo para eliminar\n")#pregunta cual quiere eliminar el usuario
            pregunta = str(pregunta)
            
            #cuando el usuario elija una opcion para eliminar se elimina uno
            if pregunta=="1":
                suma1=suma1-1
            if pregunta=="2":
                suma2=suma2-1
            if pregunta=="3":
                suma3=suma3-1

        #contador para cada platillo
        if combo=="1":
            combo=int(combo)
            suma1=suma1+combo
        if combo=="2":
            combo=int(combo)
            suma2=suma2+combo-1#se resta uno debido al string
        if combo=="3":
            combo=int(combo)
            suma3=suma3+combo-2#se resta dos debido al string
        combo = input("*******************************************************\n"
                          "            BIENVENIDO AL RESTAURANTE\n"
                          "*******************************************************\n"
                          "COMBO 1: 3 tacos al pastor y 1 bebida............Q15.00\n"
                          "COMBO 2: 3 tacos de cochinita pibil y 1 bebida...Q18.00\n"
                          "COMBO 3: 2 gringas al pastor y 1 bebida..........Q25.00\n\n"
                          "Acciones que puede ejecutar:\n"
                          "- Indicar el numero del combo que desea.\n"
                          "- Ingresar 'Solamente eso' para indicar que ya termino de ordenar.\n"
                          "- Ingresar 'Modificar' si desea eliminar un item de su orden.\n")#pregunta para iniciar de nuevo con el ciclo
    else:
        print ("\n\n""el valor que ingresaste no es compatible, prueba otra vez\n\n")#error para que el usuario ingrese el valor correcto
        combo = input("*******************************************************\n"
                          "            BIENVENIDO AL RESTAURANTE\n"
                          "*******************************************************\n"
                          "COMBO 1: 3 tacos al pastor y 1 bebida............Q15.00\n"
                          "COMBO 2: 3 tacos de cochinita pibil y 1 bebida...Q18.00\n"
                          "COMBO 3: 2 gringas al pastor y 1 bebida..........Q25.00\n\n"
                          "Acciones que puede ejecutar:\n"
                          "- Indicar el numero del combo que desea.\n"
                          "- Ingresar 'Solamente eso' para indicar que ya termino de ordenar.\n"
                          "- Ingresar 'Modificar' si desea eliminar un item de su orden.\n")#pregunta para iniciar de nuevo con el ciclo

propina = input("\n\n""desea incluir propina? Indicar el porcentaje o no para no incluirla.\n")

if propina =="no":#condicion para que cuando escriba no propina se cero
    propina=0
else:
    propina=float(propina)

#multiplicando el numero de platillos pedido
total1 = suma1*15
total2 = suma2*18
total3 = suma3*25

#sumando el total de platillos pedidos
subtotal=total1+total2+total3
numeroPropina=propina/100#sacando el numero de porcentaje de propina
porcentajePropina= subtotal*numeroPropina#calculando la propina
total=subtotal+porcentajePropina#calculando el total de el pedido

print("------------------------------------------------------------------\n"
          "                         RESUMEN ORDEN\n"
          "------------------------------------------------------------------\n"
          "Cantidad      Descripcion       Precio unitario       Total\n",
          suma1, "           COMBO 1           Q15.00                Q.""{0:.2f}".format(total1),"\n",
          suma2, "           COMBO 2           Q18.00                Q.""{0:.2f}".format(total2),"\n",
          suma3, "           COMBO 3           Q25.00                Q.""{0:.2f}".format(total3),"\n"
          "------------------------------------------------------------------\n"
          "Subtotal                        Q.""{0:.2f}".format(subtotal),"\n"
          "Propina                         Q.""{0:.2f}".format(porcentajePropina),"\n"
          "TOTAL                           Q.""{0:.2f}".format(total),"\n")#sacando el total a pagar



