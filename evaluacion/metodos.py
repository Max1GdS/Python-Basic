mensaje = "parte 1 del mensaje"
mensaje += "parte 2 del mensaje"

print(mensaje)
num=0
lista = []
print("este programa sigue la sucesion numerica")
n=int(input("cuantos numeros quieres de la sucecion numerica ?: "))
b=3
num=int(b)
lista.append(num)
res=0
n=n-1
while n>0:
    res=b**2
    num=int(res)
    lista.append(num)
    n=n-1
    b=b**2
    if n>0:
        res=b*2
        num=int(res)
        lista.append(num)
        n=n-1
        b=b*2
        if n>0:
            res=res-2
            num=int(res)
            lista.append(num)
            n=n-1
            b=b-2
print("lista : ",lista)
print("fin del programa, gracias por utilizarlo")
