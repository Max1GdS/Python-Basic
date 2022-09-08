print("""este programa hace un calculo dependiendo tu numero , 
si es par lo eleva al cuadrado y si es impar lo eleva al cubo""")
a = input("ingresa tu numero: ")
numero = float(a)
if numero % 2 == 0:
    print("realizaremos el calculo")
    b = numero*numero
    print("tu numero se elevo al cuadrado, el resultado es: " + str(b))
else :
    print("realizaremos el calculo")
    c = numero*numero*numero
    print("tu numero se elevo al cubo, el resultado es: " +str(c))
print("fin del programa")

