import random 
print("este es un juego de adivinanza , nuestra computadora escoge un numero entre el 0 - 100 y ")
print("tienes 6 intentos para adivinar, te daremos pistas casi es mayor o menor del numero al azar")
a = (random.randrange(0,100))
n = 6
while n > 0:
    b = int(input("que numero es ?: "))
    n -= 1
    if a == b:
        print("--->es el correcto, haz ganado :)")
        n = -1
    else:
        print("te quedan ",n,"intentos")
        if b > a:
            print("--->el numero es menor")
        else:
            print("--->el numero es mayor")
if a != b:
    print("se acabaron tus intentos")
print("el numero al azar es: ",a)
print("fin del programa, gracias por participar")
