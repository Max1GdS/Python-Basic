# Generar un algoritmo que lea 
# tres números distintos, para que 
# luego se muestre cuál es el valor
# mayor, cuál es el menor, y 
# cuál es el intermedio.(10 pts)

print("este programa descubrira cual es tu numero mayor,menor y intermedio")
a = float(input("ingresa un numero: "))
b = float(input("ingresa otro numero: "))
c = float(input("ingresa otro numero: "))
if a == b == c:
    print("los tres numeros son iguales")
    print("el maximo,minimo y intermedio ese: ",str(a))
elif a < b > c:
    print("tu numero mayor es: ",str(b))
    if a < c:
        print("tu numero intermedio es: ",str(c))
        print("tu numero menor es: ",str(a))
    else:
        print("tu numero intermedio es: ",str(a))
        print("tu numero menor es: ",str(c))
elif b < a > c:
    print("tu numero mayor es: ",str(a))
    if b < c:
        print("tu numero intermedio es: ",str(c))
        print("tu numero menor es: ",str(b))
    else:
        print("tu numero intermedio es: ",str(b))
        print("tu numero menor es: ",str(c))
elif a < c > b:
    print("tu numero mayor es: ",str(c))
    if a < b:
        print("tu numero intermedio es: ",str(b))
        print("tu numero menor es: ",str(a))
    else:
        print("tu numero intermedio es: ",str(a))
        print("tu numero menor es: ",str(b))
elif a == b < c:
    print("el numero mayor es: ",str(c))
    print("el numero menor y intermedio es: ",str(a))
elif c == b < a:
    print("el numero mayor es: ",str(a))
    print("el numero menor y intermedio es: ",str(b))
elif a == c < b:
    print("el numero mayor es: ",str(b))
    print("el numero menor y intermedio es: ",str(a))
elif a == b > c:
    print("el numero mayor y intermedio es: ",str(b))
    print("el numero menor: ",str(c))
elif c == b > a:
    print("el numero mayor y intermedio es: ",str(b))
    print("el numero menor es: ",str(a))
elif a == c > b:
    print("el numero mayor y intermedio es: ",str(a))
    print("el numero menor es: ",str(b))
else:
    print("error")
print("fin del programa, gracias por utilizar el programa")




