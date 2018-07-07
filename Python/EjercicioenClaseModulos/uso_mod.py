from  mod import sueldo_trabajadores

a = int(input("ingresar numero"))
b = int(input("ingresar porcentaje de bono"))
c = int(input("ingresar numero de aguinaldo"))
valor = sueldo_trabajadores(a,b,c)
print("   igss   iva  bono   aguinaldo  total\n",valor)

