#un round: la copu genera un numero aleatorio y pide al usuario que
#lo adivine El usuario ingresa un numero y la maquina responde si es
#mayor menor o igual



respuesta = 0
while(respuesta==0):
    from random import randint
    a = randint(0,100)
    print (a)
    pregunta = input("adivine el numero\n")
    pregunta = int(pregunta)
    if pregunta<a:
        print ("menor")
    elif pregunta>a:
        print ("mayor")
    else:
        print("igual")
    
    

    


