print("sirve para contar los numeros postivos que ingresan")
i = 1
contador=0
while i <= 1000000000000:
    a = float(input("ingresa tus numeros : "))
    print("si no quieres ingresar mas numeros,ingresa un 0")
    if a > 0:
        contador= contador + 1
        i=i+1
    elif a < 0:
        i=i+1
    else:
        print("no puedes ingresar mas numeros,el total de positivos es: ",contador)
print("gracias por utilizar el programa")    
