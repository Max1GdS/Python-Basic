import random 
print("")
print("este es un juego de adivinanza , usted escoge un numero entre el 0 - 100 y ")
print("el computador tiene 6 intentos para adivinar, le daremos pistas casi es mayor")
print("o menor del numero al azar")
print("")
print("'''''''sigue las intrucciones'''''''")
print("--->piensa en un numero del 0 - 100 ")
pregunta=input("si estas listo escribe (si) : ")
a =  (random.randint(0,100))
n = 6
c = 0
x=0
y=100
contador=1
print("si es mayor a su numero escribe (+) , si es menor escriba (-), si la maquina adivino escriba (=)")
a =  (random.randint(0,100))
print(a, "--> intento N° 1")
while n > 1:
    b = input("escriba el signo que corresponde :")
    n -=1
    contador += 1
    if b == "+":
        x = a
        c = random.randint(x,y)
        print(c,"--> intento N°",contador)
        a = c
    elif b == "-":
        y = a
        c = random.randint(x,y)
        print(c, "--> intento N°",contador)
        a = c
    elif b == "=":
        print("----> numero adivinado :) ")
        n = -1
    else:
        print("---> ¡signo invalido! ")
        n += 1
if n == 1:
    b = input("escriba el signo que corresponde :")
    if b == "=":
        print("----> numero adivinado :) ")
    else:
        print("no pudimos adivinar tu numero")
else:
    print("fin")
print("gracias por participar")