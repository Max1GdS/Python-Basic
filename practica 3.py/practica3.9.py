print("este programa calculara una ecuacion con dos variables")
a = float(input("introduce la variable a: "))
b = float(input("introduce la variable b: "))
x = 0
if a != 0:
    x = -b / a
    print("la solucion unica es : ",x)
elif a == 0 and b != 0:
    print("no tiene solucion")
elif a == 0 and b == 0:
    print("tiene soluciones infinitas")
else:
    print("error")