#Obtener la serie: 1,-1,2,-2,3,-3,… para n números 

print("este programa sirve para descubrir la serie numerica")
b=1
res=0
a=int(input("cuantos numeros quieres de la serie: "))
lista = []
lista.append(b)
a=a-1
while a > 0:
    res=b*-1
    lista.append(res)
    if a > 0:
        a=a-1
        b=b+1
        if a>0:
            lista.append(b)
            a=a-1
print("lista : ",lista)
print("fin del programa,gracias por utilizarlo")
    #res=b*-1
    #print(res)
    #b=b+1
    #print(b)
    #a=a-1

