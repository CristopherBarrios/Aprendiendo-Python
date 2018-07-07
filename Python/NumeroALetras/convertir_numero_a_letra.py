#uso_convertir_numero_a_letra.py
# lunes 5 de mar del 2018
#cristopher jose rodolfo barrios solis
#18207
#tarea

def convertir(num1):

    #estas variables sirven para indicar cual texto va a hacer, en el programa se utilizan varios
    #operaciones matematicas para indicar que espacio es, si da uno va a elegir el segundo espacio
    unidades = ["cero", "uno", "dos" ,"tres" ,"cuatro" ,"cinco" ,"seis" ,"siete" ,"ocho" ,"nueve","diez"]
    dieci = ["once", "doce","trece","catorce", "quince","diezciseis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["veinte", "treinta","cuarenta","cincuenta", "sesenta","setenta", "ochenta", "noventa","cien"]
    
    if (num1 >=0 and num1 <11):#condicion para saber el rango de unidads
        respuesta = unidades[num1]#muestra cual espacio se va a utilizar de la variable
        return respuesta
    elif (num1 < 20):#condicion para escribir los del once hasta diecinueve
        respuesta = dieci[num1-11]#muestra cual espacio se va a utilizar de la variable y se le resta once 
        return respuesta
    elif num1<101:
       segundoNumero = num1% 10;#saber cual es el primer digito
       primerNumero = int(num1/10)#saber cual es el segundo digito
       if (segundoNumero == 0):#condicion para que no diga veinte y cero
           respuesta = decenas[primerNumero-2]
           return respuesta
       else:
           paso1=decenas[primerNumero-2]
           paso2=unidades[segundoNumero]
           respuesta = paso1+" y " + paso2#suma para que la respuesta salga bien con el print
           return respuesta
    else:
        print ("Ingrese en el rango solicitado")
        
        
