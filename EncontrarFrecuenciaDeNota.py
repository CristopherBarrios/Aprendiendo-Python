#cristopher jose rodolfo barrios solis
#18207

preguntaNota=input("ingrese la nota A, B, C, D, F o G\n")#preguntando la nota que quiera el usuario
preguntaOctava=input("ingrese la octava de 0-8\n")#ingresando la octava que desee el usuario


while preguntaOctava !="fin":#centinela, al poner fin que termine de preguntar
    
    preguntaOctava=int(preguntaOctava)

    #definiendo una condicion que si ingresa una nota
    #la variable nota sera la correspondiente
    if preguntaNota=="c":
        Nota=261.63
    if preguntaNota=="d":
        Nota=293.66
    if preguntaNota=="e":
        Nota=329.63
    if preguntaNota=="f":
        Nota=349.23
    if preguntaNota=="g":
        Nota=392.00
    if preguntaNota=="a":
        Nota=440.00
    if preguntaNota=="b":
        Nota=493.88

        #definiendo tambien en mayusculas
        #por si el usuario lo ingresa diferente
    if preguntaNota=="C":
        Nota=261.63
    if preguntaNota=="D":
        Nota=293.66
    if preguntaNota=="E":
        Nota=329.63
    if preguntaNota=="F":
        Nota=349.23
    if preguntaNota=="G":
        Nota=392.00
    if preguntaNota=="A":
        Nota=440.00
    if preguntaNota=="B":
        Nota=493.88

    #generando una condicion para que el usuario ingrese
    #dentre de el rango que pide
    if preguntaOctava>0 and preguntaOctava<8:
        operacion1=4-preguntaOctava
        operacion2=2 ** operacion1
        operacion3=Nota/operacion2
        print(preguntaNota,preguntaOctava,"tiene una frecuencia de", operacion3,"\n\n")
    else:
        print("favor de ingresar un valor dentro del rango 0-8\n\n")
        
#preguntando al usuario si quiere seguir consultando notas o que escriba fin para terminar
    preguntaNota=input("ingrese la nota A, B, C, D, F o G\n")
    preguntaOctava=input("ingrese la octava de 0-8 o escriba fin para terminar\n")
    

