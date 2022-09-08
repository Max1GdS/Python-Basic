print("este programa simula una clave , clave: iloveyou123 , si se equivoca la pedira denuevo")
a = "iloveyou123"
n=1
while n > 0:
    b = str(input("introduce la clave: "))
    if a == b:
        print("contraseña correcta, gracias por utilizar el programa")
        n=0
    elif a != b:
        print("vuelve a intentarlo")
        n=n+1
    else:
        print("error")
print("FIN")

