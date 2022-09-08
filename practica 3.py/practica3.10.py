print("este programa determina que tamaño tiene un tornillo respecto a sus centimetros")
a = float(input("cuanto mide tu tornillo en cm : "))

if a >= 1 and a < 3:
    print("tu tornillo tiene tamaño pequeño")
elif a >= 3 and a < 5:
    print("tu tornillo tiene tamaño mediano")
elif a >= 5 and a < 6.5:
    print("tu tornillo tiene tamaño grande")
elif a >= 6.5 and a < 8.5:
    print("tu tornillo tiene tamaño muy grande")
else:
    print("no existe")
