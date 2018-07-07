#cristopher jose rodolfo barrios solis
#18207

def comparar_cartas(uno,dos,num1,num2,num3,num4,num5):#comparando las cartas de la mano del jugador y de la mesa
    #comparando por trios
    if(uno==num1 and uno==num2)or(uno==num1 and uno==num3)or(uno==num1 and uno==num4)or(uno==num1 and uno==num5)or(uno==num2 and uno==num3)or(uno==num2 and uno==num4)or(uno==num2 and uno==num5)or(uno==num3 and uno==num4)or(uno==num3 and uno==num5)or(uno==num4 and uno==num5)or(dos==num1 and dos==num2)or(dos==num1 and dos==num3)or(dos==num1 and dos==num4)or(dos==num1 and dos==num5)or(dos==num2 and dos==num3)or(dos==num2 and dos==num4)or(dos==num2 and dos==num5)or(dos==num3 and dos==num4)or(dos==num3 and dos==num5)or(dos==num4 and dos==num5)or(uno==dos and uno==num1)or(uno==dos and uno==num2)or(uno==dos and uno==num3)or(uno==dos and uno==num4)or(uno==dos and uno==num5):
        respuesta = 16#puntaje por trios
        return respuesta
    #comparando por duos
    elif uno==num1 or uno==num2 or uno==num3 or uno==num4 or uno==num5 or dos==num1 or dos==num2 or dos==num3 or dos==num4 or dos==num5 or uno==dos:
        respuesta = 15#puntaje por duos
        return respuesta
    else:#comparando solo los de la mano en en caso que no hayan trios ni duos
        if uno > dos:
            respuesta = uno
            return respuesta
        else:
            respuesta = dos
            return respuesta
def convertir(num):#convirtiendo las letras a numeros
    if num == "J":
        numero = 11
        return numero
    if num == "Q":
        numero = 12
        return numero
    if num == "K":
        numero = 13
        return numero
    if num == "A":
        numero = 14
        return numero
    return num

def ganador(num1,num2):#busca quien de los jugadores tiene mayor puntaje
    if num1 > num2:
        respuesta = "El ganador es el jugador uno"
        return respuesta
    else:
        respuesta = "El ganador es el jugador dos"
        return respuesta

