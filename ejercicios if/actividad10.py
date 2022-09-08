print("este programa sirve para calcular el maximo de 3 numeros")
a = float(input("ingresa tu primer numero : "))
b = float(input("ingresa tu segundo numero : "))
c = float(input("ingresa tu tercer numero : "))

if b < a > c:
    print("el maximo es tu primer numero : "+str(a))
elif a < b > c:
    print("el maximo es tu segundo numero : "+str(b))
elif a < c > b:
    print("el maximo es el tercer numero : "+str(c))
elif a == b == c:
    print("tu tres numeros son iguales, el maximo es :"+str(a))
elif a == b < c:
    print("el maximo ees tu tercer numero : "+str(c))
elif a == c < b:
    print("el maximo es tu segundo numero : "+str(b))
elif c == b < a:
    print("el maximo es tu primer numero : "+str(a))
else :
    print("error")

