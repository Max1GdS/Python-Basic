import time
print('bienvenido a A.S.A.R.')
print('este juego consiste en que ud proporcione un numero al azar entre 0 y 100, y el ordenador intentara adivinarlo \npara ello el ordenador dispone de 6 intento validos,si los sobrepasa GAME OVER')
time.sleep(4)
a=int(input('escriba aqui su numero: '))
import random 
#variables
cero=0
cien=100
intento=1
if a in range(0,100):
    while intento <= 6: #<--------------------------------------intentos permitidos
        print('*intento numero* :',intento)
        print('ordenador intentando adivinar')
        time.sleep(2) # loading jaja
        r =  (random.randint(cero,cien))
        print(r)
        if r == a:
            print('¡EL ORDENADOR LO A LOGRADO!')
            intento=7
        elif r > a:  #<---------------------------------------mayor
            print('INCORRECTO')
            if intento == 7:
                print('*nuevamente*') 
            cien=r 
            intento+=1
        elif r < a:  #<---------------------------------------menor
            print('INCORRECTO')
            if intento == 7:
                print('*nuevamente*') 
            cero=r
            intento+=1
    if intento == 7:
            print ("****GAME OVER****")
    time.sleep(3)
    print('FIN DEL PROGRAMA')
else:
    print('***numero invalido***\n***FIN DEL PROGRAMA***')