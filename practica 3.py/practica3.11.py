print("este programa sirve para calcular la media de dos puntos enteros y descubrir el cuadrante que pertenece")
ax = int(input("introduce el valor de ax: "))
ay = int(input("introduce el valor de ay: "))
bx = int(input("introduce el valor de bx: "))
by = int(input("introduce el valor de by: "))
pmx=(ax+bx)/2
pmy=(ay+by)/2
print("el punto medio es ",round(pmx),",",round(pmy))
if pmx == 0 and pmy == 0:
    print("es el punto de interseccion, es 0,0")
elif pmx > 0 and pmy > 0:
    print("pertenece al cuadrante 1")
elif pmx < 0 and pmy > 0:
    print("pertenece al cuadrante 2")
elif pmx < 0 and pmy < 0:
    print("pertenece al cuadrante 3")
elif pmx > 0 and pmy < 0 :
    print("pertenece al cuadrante 4")
else:
    print("no pertenece a ningun cuadrante")
print("Fin del programa")