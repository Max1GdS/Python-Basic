print("este programa descubrira que tipo de triangulo es solo con los lados")
a = float(input("introduce un lado: "))
b = float(input("introduce un lado: "))
c = float(input("introduce un lado: "))
if a == b == c:
    print("todos sus lados son iguales, es un triangulo equilatero")
elif a == b or a == c or b == c:
    print("tiene dos lados iguales, es un triangulo isoceles")
else:
    print("tiene los tres lados diferentes, es un triangulo escaleno")
