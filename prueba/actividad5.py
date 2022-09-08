#Escribir un algoritmo que pida una password numérica y 
# con un máximo de tres intentos. Si se ingresa la contraseña correcta
# , que se muestre "usuario autenticado". En caso contrario,
#  el programa debe mostrar " Contraseña Incorrecta"
# Posteriormente terminar el programa de inmediato.
intentos=3
print("este programa simula el registro")
print("comenzamos con la creacion de la cuenta")
a = str(input("¿como te quieres llamar? "))
b = int(input("¿que clave quieres utilizar?"))
print("cuenta creada con exito, ingresa a tu cuenta")
while intentos > 0:
    c = str(input("ingresa tu usuario: "))
    d = int(input("ingresa tu clave: "))
    if c == a and d == b:
        print("haz ingresado con exito")
        intentos=0
    else:
        print("usuario o contraseña incorrecta")
    intentos=intentos-1
print("fin del programa")
