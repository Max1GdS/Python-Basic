#2. Determinar si un año ingresado
#  por el usuario, es bisiesto.(10 pts)
print("este programa te ayudara a ver cuando es el año bisiesto")
a=int(input("ingresa un año: "))
if a % 4 == 0 and a % 100 !=0:
    print("el año es bisiesto")
elif a % 4 == 0 and a % 100 ==0 and a % 400 == 0:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")
print("fin del programa")
