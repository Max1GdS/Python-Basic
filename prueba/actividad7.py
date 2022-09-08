#Escribir un programa que permita obtener el valor aproximado de PI, 
# mediante la serie: 4 - 4/3 + 4/5 – 4/7 + 4/9 – 4/11 + … para n términos.
print("este programa sirve para el calculo de pi mediante una serie de procedimientos")
lista = []
n = int(input("cuantos numeros quieres de la serie ?: "))
res = 4
b=3
n=n-1
lista.append(res)
while n > 0:
    res = res - (4/b)
    b=b+2
    lista.append(res)
    n=n-1
    if n>0:
        res = res +(4/b)
        b=b+2
        lista.append(res)
        n=n-1
print("lista : ",lista)
print("fin del programa")