print("calcula la media de tus numeros positivos")
a = int(input("¿cuantos numeros vas a ingresar? :"))
i=1
resultado = 0
res = 0
for i in range (a):
    b = int(input("introduce tus numeros"))
    res = res + b
    i = i + 1
resultado = res / a 
print("la media de tus numeros es :",str(resultado) )
