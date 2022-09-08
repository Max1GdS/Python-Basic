import time
print ('este programa ordenara los numero  que ingrese de forma ansendente')
lista=[]
n=int(input('ingrese cualquier numero(si no desea ingresar mas numeros digite "0"): '))
lista.append (n)
while n != 0:
    n=int(input('ingrese cualquier numero(si no desea ingresar mas numeros digite "0"): '))
    lista.append (n) # <---- convertiendo los digitos del bucle en una lista
print('***ORDENADO NUMEROS***')
time.sleep(3)
lista.sort()
lista.pop(0)
print (lista)
time.sleep(10)
print('FIN DEL PROGRAMA')