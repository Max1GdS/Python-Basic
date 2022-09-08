list = []
print()
print("este programa calculara su digito verificador , siga las intrucciones para un funcionamiento correcto.")
print("si su rut no tiene 8 digitos , introduzca un 0 al inicio, gracias por su comprension.")
n=8
ResSuma=0
while 0 < n:
    rut = int(input("introduce los numeros de su rut en orden uno por uno sin puntos:  "))
    list.append(rut)
    n -= 1
def calculodig(list):
    res1=list[0]*3
    res2=list[1]*2
    res3=list[2]*7
    res4=list[3]*6
    res5=list[4]*5
    res6=list[5]*4
    res7=list[6]*3
    res8=list[7]*2
    resultado_suma=res1+res2+res3+res4+res5+res6+res7+res8
    modulo=resultado_suma%11
    digito=11-modulo
    return digito
dig=calculodig(list)
valores = " ".join(list)
print("su rut es ",list)
if dig > 0 and dig <10:
    print("el digito verificador de su rut es: ",dig)
elif dig == 11:
    print("el digito verificador de su rut es: 0")
else:
    print("el digito verificador de su rut es: K")
print("FIN DEL PROGRAMA.")