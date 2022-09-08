a = int(input("cuantos años tiene su perro: "))
edad = 0
if a <= 2:
    edad = a * 10.5 
    print("la edad de su perro en equivalencia humana es ",edad," años")
elif a > 2:
    edad = 2 * 10.5 + (a - 2)*4
    print("la edad de su perro en equivalencia humana es ",edad," años")
else:
    print("el programa solo permite numeros enteros")