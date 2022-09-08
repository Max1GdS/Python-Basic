#ejercicios obligatorios practica 3.1
A=int(input("introduce el producto A: "))
B=int(input("introduce el producto B: "))
C=int(input("introduce el producto C: "))
#saber casi el producto A es el mas elevado
if B < A > C:
    print("A es el valor mas elevado")
else:
    print("A no es el valor mas elevado")
#saber casi un producto es menor a 200
if A < 200 and B < 200 and C < 200:
    print("pueden haber un producto o mas,con ventas menores a 200")
else:
    print("ningun producto tiene ventas menor a 200")
#saber casi un producto es mayor a 400
if A < 400 and B < 400 and C < 400:
    print("ningun producto tiene ventas que superan los 400")
else:
    print("un producto o mas supera los 400")
#saber casi la media de ventas es superior a 500
if (A + B + C ) / 3 <= 500:
    print("la media de ventas no supera los 500")
else:
    print("la media de ventas es superior a los 500")
if A < B > C:
    print("el producto que tiene mas ventas es B")
else:
    print("el producto B no es el que tiene mas ventas")
if (A + B + C) >= 500 and (A + B + C) <= 1000:
    print("el total de las ventas estan entre 500-1000")
else:
    print("el total de las ventas no estan entre 500-1000")






