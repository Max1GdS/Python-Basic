print("*****************************************************************************")
print("* nuestro programa sirve para ordenar N numeros enteros de forma ascendente *")
print("*****************************************************************************")
n=int(input("cuantos numeros vas a ingresar ?: "))
lista=[]
while n > 0:
    num = int(input("ingresa tu numero : "))
    lista.append(num)
    n -= 1
ascend = sorted(lista)
print(ascend)