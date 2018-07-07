#cristopher jose rodolfo barrios solis
#18207



#inicialisando las variables
canivalDer = 3#otorgando valor a los canivales
misioneroDer = 3#otorgando valor a los misioneros
canivalIz = 0
misioneroIz = 0
canivalBote=0
misioneroBote=0
bote=0
x=0
y=0
while (x!=6 or y<14):#ciclo que repite en que parte ir del rio
    #lado derecho
    pregunta1 = input("que desea llevar al bote\n""canival o misionero:\n")#pregunta del centinela
    while (pregunta1 !="crusar a la izquierda"):#centinela
        bote=canivalBote+misioneroBote#suma el total de personajer que estan en el bote
        if pregunta1 == "sacar del bote":#consulta para sacar los personajes del bote
            if bote==1 or bote==2:
                pregunta2= input("que desea sacar\n""canival o misionero:\n")
                #condiciones para sacar el personaje del bote
                if pregunta2=="canival":
                    if canivalBote==1 or canivalBote==2:
                        canivalBote=canivalBote-1
                        canivalDer = canivalDer +1
                    else:
                        print ("no hay ningun canival")
                if pregunta2=="misionero":
                    if misioneroBote==1 or misioneroBote==2:
                        misioneroBote=misioneroBote-1
                        misioneroDer = misioneroDer + 1
                    else:
                        print("no hay ningun misionero")
            else:
                print("no hay nadie en el bote para poder sacarlo")
        if bote<2:#condicion para que solo acepte 2 personajes en el bote
            if pregunta1=="canival":
                canivalDer = canivalDer -1
                canivalBote = canivalBote + 1#agregando un personaje al bote
            if pregunta1=="misionero":
                misioneroDer = misioneroDer -1
                misioneroBote = misioneroBote + 1
        else:
            print("ya no se pueden agregar mas al bote")
        print("\n""Canivales Derecha:\n",canivalDer,"\n"
          "Misioneros derecha:\n",misioneroDer,"\n"
          "Canivales en el bote:\n",canivalBote,"\n"
          "Misioneros en el bote:\n",misioneroBote,"\n"
          "Canivales izquierda:\n",canivalIz,"\n"
          "Misionero izquierda:\n",misioneroIz,"\n")#imprimiendo el resultado para guiar al jugador
        pregunta1 = input("que desea llevar al bote\n""canival o misionero o crusar a la izquierda o sacar del bote:\n")#pregunta del centinela
        #lado izquierdo
    pregunta3 = input("que desea hacer\n""canival o misionero o crusar a la derecha o sacar del bote\n")#pregunta del centinela del lado izquierdo
    while (pregunta3 != "crusar a la derecha"):#ciclo para repetir lo que quiere hacer el jugador
        bote=canivalBote+misioneroBote#suma la cantidad de personajes en el bote
        if pregunta3 == "sacar del bote":
            if bote==1 or bote==2:#condicion para que solo acepte que esten en el bote
                pregunta2= input("que desea sacar\n""canival o misionero:\n")
                if pregunta2=="canival":
                    if canivalBote==1 or canivalBote==2:
                        canivalBote=canivalBote-1#restando canivales
                        canivalIz = canivalIz +1#sumando canivales a la izquierda
                    else:
                        print ("no hay ningun canival")
                if pregunta2=="misionero":
                    if misioneroBote==1 or misioneroBote==2:
                        misioneroBote=misioneroBote-1
                        misioneroIz = misioneroIz + 1
                    else:
                        print("no hay ningun misionero")
            else:
                print("no hay nadie en el bote para poder sacarlo")
        if bote<2:#condicion para que no acepte mas de 2 en el bote
            if pregunta3=="canival":
                canivalIz = canivalIz -1
                canivalBote = canivalBote + 1
            if pregunta3=="misionero":
                misioneroIz = misioneroIz -1
                misioneroBote = misioneroBote + 1
        else:
            print("ya no se pueden agregar mas al bote")
        print("\n""Canivales Derecha:\n",canivalDer,"\n"
          "Misioneros derecha:\n",misioneroDer,"\n"
          "Canivales en el bote:\n",canivalBote,"\n"
          "Misioneros en el bote:\n",misioneroBote,"\n"
          "Canivales izquierda:\n",canivalIz,"\n"
          "Misionero izquierda:\n",misioneroIz,"\n",)#guia para que el usuario juegue
        x=misioneroIz+canivalIz
        y=y+1
        pregunta3 = input("que desea hacer\n""canival o misionero o crusar a la derecha o sacar del bote\n""si ya logro terminar el juego cruse a la derecha para terminar")
print("Game over")#muestra que el juego a terminado
    


