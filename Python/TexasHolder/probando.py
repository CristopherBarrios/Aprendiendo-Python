from moduloTexasHoldem import comparar_cartas, convertir_jeje

uno = 7
dos = 2
num1 = 3
num2 = 10
num3 = 5
num4 = 6
num5 = 11

num = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

num.pop(10)
num.pop(11)
num.pop(12)


num.insert(9,11)
num.insert(10,12)
num.insert(11,13)
num.insert(12,14)

print(num)

loco = comparar_cartas(uno,dos,num1,num2,num3,num4,num5)
print(loco)
