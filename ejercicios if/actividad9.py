print("este programa sirve para descubrir el maximo de dos numeros")
a = input("escribe un valor: ")
numero = float(a)
b = input("escribe otro valor: ")
numero_dos = float(b)
if numero==numero_dos:
    print("lo dos valor son iguales , el maximo es :"+ str(int(numero)))
elif numero < numero_dos:
    print("el maximo es "+ str(int(numero_dos)) +", tu segundo valor")
else :
    print("el maximo es "+ str(int((numero))) + ", tu primer valor")
print("gracias por utilizar este programa")