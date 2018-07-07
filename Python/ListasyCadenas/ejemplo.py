miCadena = "EsTa Cadema EsTa AlGo RaRa"
miLista = miCadena.split(" ")

for palabra in miLista:
    palabra = palabra.upper()
    print("analizando la palabra:",palabra)
    print("\tLa palabra tiene"+ str(len(palabra))+ "caracteres de largo")

    if len(palabra)%2==0:
        print("\tLa cantidad de letras es un numero par")
    else:
        print("\tLa cantidad de letras es un numero impar")

    print("\tLa primera letra de la palabra es:", palabra[0])
    print("\tLa ultima letra dela palabra es:", palabra[-1])
