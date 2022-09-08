import time
print('bienvenido a A.S.A.R.')
print('este juego consiste en que ud adivine un numero random entre 0 y 100, \npara ello ud dispondra de 6 intento validos,si los sobrepasa GAME OVER')
time.sleep(6)
print('generando numero al azar')
time.sleep(1) # loading jaja
print('generando numero al azar')
time.sleep(1) # loading jaja
print('generando numero al azar')
time.sleep(1) # loading jaja
import random 
r =  (random.randint(0,100))
print('listo!')
intento=1
while intento <= 6: #<--------------------------------------intentos permitidos
    print('*intento numero* :'+str(intento))
    a=int(input('ahora escriba un numero (del 0 al 100): '))
    if a == r:
        print('***FELICIDADES***')
        intento=8
    elif a > r:  #<---------------------------------------mayor
        print('INCORRECTO')
        print('*PISTA: MAS ABAJO*') 
        if intento == 7:
            print ("GAME OVER") 
        intento+=1
    elif a < r:  #<---------------------------------------menor
        print('INCORRECTO')
        print('*PISTA: DALE MAS* ')   
        intento+=1
if intento == 7:
            print ("****GAME OVER****")
            print ('el numero al azar era: ',r,'\n ヘ(-_-;)  INTENTELO NUEVAMENTE')
if intento == 8:
    print('WINNER WINNER CHICKEN DINNER')
    print('usted a GANADO')
time.sleep(3)
print('FIN DEL PROGRAMA')