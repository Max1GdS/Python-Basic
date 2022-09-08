print("este programa sirve para ver que su numero tiene un modulo menor a 15")
a = input("ingrese un numero: ")
numero = float(a)
if numero > 0 :
    print("haremos el calculo")
    c = numero * numero / numero
    if c < 15:
        print("el modulo es menor a 15")
        print("tu modulo es : " , c )
    elif c==15:
        print("tu modulo es igual que 15")
        print("tu modulo es : " , c )
    else:
        print("tu modulo es mayor a 15")
        print("tu modulo es : " , c )
elif numero == 0:
    print("tu modulo es 0")
    print(" y tu modulo es menor a 15")
else :
    print("haremos el calculo")
    f = numero * -1
    if f < 15:
        print("tu modulo es menor que 15")
        print("tu modulo es : " , f )
    elif f==15:
        print("tu modulo es igual que 15")
        print("tu modulo es : " , f )
    else:
        print("tu numero es menor que 15")
        print("tu modulo es : " , f )

