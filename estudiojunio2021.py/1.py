a = int(input("ingresa un numero para calcular el factorial:-->  "))
def factorial(a):
    sumatotal=1
    while a > 1:
        sumatotal = sumatotal*a
        a = a - 1
    return sumatotal
sumatotal = factorial(a)
print("el resultado es --> ",sumatotal)


    