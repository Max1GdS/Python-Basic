#actividad 8
print("este programa sigue la sucesión numérica : 3, 9, 18, 16, 256, 512, 510, 260100, 520200, 520198..")
print("luego suma el total de los números que quieres")
n=int(input("cuantos números quieres de la sucesión numérica ?: "))
b=3
suma=0
suma=suma+b
res=0
print(b)
n=n-1
while n>0:
    res=b**2
    print(res)
    suma=suma+res
    n=n-1
    b=b**2
    if n>0:
        res=b*2
        print(res)
        suma=suma+res
        n=n-1
        b=b*2
        if n>0:
            res=res-2
            print(res)
            suma=suma+res
            n=n-1
            b=b-2
print("la suma total de lo números que querías es de: ",str(suma))
print("fin del programa, gracias por utilizarlo")












































