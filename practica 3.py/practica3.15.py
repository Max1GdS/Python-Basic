from math import sqrt
print("este programa calcula la solucion de una ecuacion de segundo grado: ax**2 + bx + c = 0")
a=float(input("ingresa el valor de a: "))
b=float(input("ingresa el valor de b: "))
c=float(input("ingresa el valor de c: "))
dis=b**2-4*a*c
if a == 0:
    x = -c/b
    print("el resultado de su ecuacion es: ",x)
elif dis > 0:
    x1 = (-b + sqrt(dis))/(2*a)
    x2 = (-b - sqrt(dis))/(2*a)
    print("el resultado de su ecuacion es: ")
    print("x1 : ","{:.2f}".format(x1))
    print("x2 : ","{:.2f}".format(x2))
elif b**2-4*a*c < 0:
    x1 = (-b + sqrt(dis))/(2*a)
    try:
        return sqrt(dis)

    except ValueError:
        print("no puede ser la 'c' mayor")
        print("Operacion erronea")
    x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    print("el resultado de su ecuacion es: ")
    print("x1 : ","{:.2f}".format(x1))
    print("x2 : ","{:.2f}".format(x2))
else:
    print("error")
print("fin del programa")
