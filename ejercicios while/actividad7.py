print("calcula la media de tus numeros positivos")
print("si ingresas un negativo o numero neutro,finaliza el programa")
i=1
contador = 0
res=0
while i <=10000000000:
    a=float(input("ingresa un valor: "))
    if a > 0:
        i=i+1
        contador=contador+1
        res=res+a
    else:   
        i=i+10000000000000000
        resultado=res/contador
print("la media de tu serie de enteros es: ",str(resultado))