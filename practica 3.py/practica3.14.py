# Crea un programa llamado ex_3_14, que pida los coeficientes a, b y c de una ecuación de
# segundo grado y calcule la solución.
# a x2 + b x + c = 0
# La formula matemática que resuelve esta ecuación es la siguiente:
# x=(−b±√b**2−4ac)/2a
# , es decir ,hay dos soluciones
# Ten en cuenta los siguientes casos especiales en la resolución:
# - Si a = 0 la ecuación es de primer grado, pero se puede calcular el resultado utilizando el
# algoritmo del ejercicio 3.9.
# - Si b2 – 4ac < 0 las raíces son imaginarias, pero se puede mostrar el resultado separando la
# parte real de la imaginaria., o bien decir que no tiene resultados reales.
# Pista: en Python, para calcular la raíz cuadrada podemos utilizar la función math.sqrt( ).
from math import sqrt
import cmath
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
    x1 = (-b + cmath.sqrt(dis))/(2*a)
    x2 = (-b - cmath.sqrt(b**2-4*a*c))/(2*a)
    print("el resultado de su ecuacion es: ")
    print("x1 : ","{:.2f}".format(x1))
    print("x2 : ","{:.2f}".format(x2))

else:
    print("solucion imaginaria")

