print("este programa sirve para calcular el producto de tus numeros enteros")

resultado = 0
a = 0
b = 1
i=1

while i in range (10000):
    a = float(input("introduce tu numero : "))
    i=i+1
    if a==0:
        i=i+10000000000000000000
    if a != 0:
        print("haremos los calculos")
        resultado = a * b
        a = b
        b = resultado
print("gracias por utilizar el programa, tu resultado es:",int(round(resultado,0)))
print("fin") 