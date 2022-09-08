print("este programa sirve para saber si tu numero es positivo y menor de 100")
a = input("escoge un valor")
numero = float(a)
if numero > 0:
    print("tu numero es positivo")
    if numero < 100:
        print("y tambien esee un numero menor que 100")
    else:
        print("y tambien es un numero menor que 100")
else:
    if numero == 0:
        print("tu numero es neutro")
    else:
        print("tu numero es negativo")
print("fin del programa")