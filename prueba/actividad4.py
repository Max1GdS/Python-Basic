#4.- Escribir un programa que lea una
#  lista de números y determine cuántos
#  son positivos, cuántos son negativos, 
# el máximo, y el mínimo.(10 pts)

print("""este programa sirve para descubrir tus numeros negativos y 
positivos, tambien sirve para ver el maximo y minimo de una lista""")
lista=[]
mayor=0
menor=0
positivos=0
negativos=0
neutros=0
i = int(input("¿cuantos numeros vas a ingresar? : "))
for x in range (i):
    num =float(input("ingresa tu numero : "))
    lista.append(num)
    if num > 0:
        positivos=positivos+1
    elif num == 0:
        neutros=neutros+1
    else:
        negativos=negativos+1
mayor = max(lista)
menor = min(lista)
print("lista: ", lista)
print("el maximo es: ",str(mayor))
print("el minimo es: ",str(menor))
print("cantidad de numeros positivos :",str(positivos))
print("cantidad de numeros neutros :",str(neutros))
print("cantidad de numeros negativos :",str(negativos))
