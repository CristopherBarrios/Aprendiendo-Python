#cristopher jose rodolfo barrios solis
#18207

from random import choice
from moduloTexasHoldem import comparar_cartas, convertir, ganador


cartas = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]#utilizando listas para el uso de las cartas


ganadasJugadorUno = 0
ganadasJugadorDos = 0
#bienvenida XD
print("Bienvenido al juego!\n""este juego es para dos jugadores")
Bienvenida = (input("Desea jugar un rato? si o no: \n"))
while(Bienvenida!="no"):#centinela
    #generando las cartas de la mesa en manera aleatoria
    primeraCarta = choice(cartas)
    segundaCarta = choice(cartas)
    terceraCarta = choice(cartas)
    cuartaCarta = choice(cartas)
    quintaCarta = choice(cartas)

    #generando las dos partas del primer jugador
    jugadorUnoPrimeraCarta = choice(cartas)
    jugadorUnoSegundaCarta = choice(cartas)
    
    #generando las dos partas del segundo jugador
    jugadorDosPrimeraCarta = choice(cartas)
    jugadorDosSegundaCarta = choice(cartas)

    #cambiando las letras de las cartas a numeros para comparar las cartas despues
    letrasaNumerosa = convertir(jugadorUnoPrimeraCarta)#se utiliza su funcion
    letrasaNumerosb = convertir(jugadorUnoSegundaCarta)
    letrasaNumerosA = convertir(jugadorDosPrimeraCarta)
    letrasaNumerosB = convertir(jugadorDosSegundaCarta)
    letrasaNumerosC = convertir(primeraCarta)
    letrasaNumerosD = convertir(segundaCarta)
    letrasaNumerosF = convertir(terceraCarta)
    letrasaNumerosG = convertir(cuartaCarta)
    letrasaNumerosH = convertir(quintaCarta)

    print("\n""Aqui estan tus cartas jugador uno\n", jugadorUnoPrimeraCarta," y ", jugadorUnoSegundaCarta)#mostrando las cartas de los jugadores
    print("\n""Aqui estan tus cartas jugador dos\n", jugadorDosPrimeraCarta," y ", jugadorDosSegundaCarta,"\n\n")
    preguntaJugadorUno1 = input("\n""Quieres retirarte jugador uno? si o no:\n")#pregunta si quiere rendirse, si dise que si pierde
    if preguntaJugadorUno1 == "no":
        preguntaJugadorDos1 = input("Quieres retirarte jugador dos? si o no:\n")
        if preguntaJugadorDos1 == "no":
            print("\n\n""FLOP, ""Cartas en mesa:\n",primeraCarta,segundaCarta,terceraCarta)#muestra las 3 primeras cartas de la mes

            
            preguntaJugadorUno2 = input("\n""Quieres retirarte jugador uno? si o no:\n")
            if preguntaJugadorUno2 == "no":
                preguntaJugadorDos2 = input("Quieres retirarte jugador dos? si o no:\n")
                if preguntaJugadorDos2 == "no":
                    print("\n\n""CUARTA CARTA, ""Cartas en mesa:\n",primeraCarta,segundaCarta,terceraCarta,cuartaCarta)#mustra otra carta de la mesa

                    
                    preguntaJugadorUno3 = input("\n""Quieres retirarte jugador uno? si o no:\n")
                    if preguntaJugadorUno3 == "no":
                        preguntaJugadorDos3 = input("Quieres retirarte jugador dos? si o no:\n")
                        if preguntaJugadorDos3 == "no":
                            print("\n\n""QUINTA CARTA, ""Cartas en mesa:\n",primeraCarta,segundaCarta,terceraCarta,cuartaCarta,quintaCarta)#muestra la quinta carta de la mesa
                            
                            preguntaJugadorUno4 = input("\n""Quieres retirarte jugador uno? si o no:\n")
                            if preguntaJugadorUno4 == "no":
                                preguntaJugadorDos4 = input("Quieres retirarte jugador dos? si o no:\n")
                                if preguntaJugadorDos4 == "no":
                                    #utiliza la funcion para comparar las cartas de la mano con las de la mesa
                                    jugadorUno = comparar_cartas(letrasaNumerosa,letrasaNumerosb,letrasaNumerosC,letrasaNumerosD,letrasaNumerosF,letrasaNumerosG,letrasaNumerosH)
                                    jugadorDos = comparar_cartas(letrasaNumerosA,letrasaNumerosB,letrasaNumerosC,letrasaNumerosD,letrasaNumerosF,letrasaNumerosG,letrasaNumerosH)
                                    winner = ganador(jugadorUno,jugadorDos)#compara el puntaje de las cartas de los jugadores
                                    print(winner)#muestra quien es el ganador
                                elif preguntaJugadorDos4 == "si":
                                    winner = "El ganador es el jugador uno"
                                    print("\n""El ganador es el jugador uno")
                                else:
                                    print("\n""Pon un valor correcto")
                            elif preguntaJugadorUno4 == "si":
                                winner = "El ganador es el jugador dos"
                                print("\n""El ganador es el jugador dos")
                            else:
                                print("\n""Pon un valor correcto")
                    
            
                        elif preguntaJugadorDos3 == "si":
                            winner = "El ganador es el jugador uno"
                            print("\n""El ganador es el jugador uno")
                        else:
                            print("\n""Pon un valor correcto")
                    elif preguntaJugadorUno3 == "si":
                        winner ="El ganador es el jugador dos"
                        print("\n""El ganador es el jugador dos")
                    else:
                        print("\n""Pon un valor correcto")
                        
            
                elif preguntaJugadorDos2 == "si":
                    winner = "El ganador es el jugador uno"
                    print("\n""El ganador es el jugador uno")
                else:
                    print("\n""Pon un valor correcto")
            elif preguntaJugadorUno2 == "si":
                winner ="El ganador es el jugador dos"
                print("\n""El ganador es el jugador dos")
            else:
                print("\n""Pon un valor correcto")
                
        elif preguntaJugadorDos1 == "si":
            winner = "El ganador es el jugador uno"
            print("\n""El ganador es el jugador uno")
        else:
            print("\n""Pon un valor correcto")
    elif preguntaJugadorUno1 == "si":
        winner = "El ganador es el jugador dos"
        print("\n""El ganador es el jugador dos")
    else:
        print("\n""Pon un valor correcto")
    if winner == "El ganador es el jugador uno":
        ganadasJugadorUno = ganadasJugadorUno + 1
    elif winner == "El ganador es el jugador dos":
        ganadasJugadorDos = ganadasJugadorDos + 1
    else:
        print("reiniciando...")
    Bienvenida = (input("\n""Desea jugar otra vez? si o no: \n"))
print("Jugador Uno:", ganadasJugadorUno,"\n""Jugador Dos:", ganadasJugadorDos)
print("Adios!")#despedida jeje XD




