import turtle
print("")
figura=input("ingresa que figura quieres (triangulo/rectangulo/circulo): " )
contador2=0
if figura=="triangulo":
    b = int(input("cual es la altura de tu triangulo?"))
    contador=b-1
    for i in range (b):
        a="/"
        c="\ "
        d=" "
        e="_"
        if i !=b-1:
            print((d*contador+a)+(d*contador2+c    ))
            contador-=1
            contador2+=2
        if i==b-1:
            contador2
            print(a+e*contador2+c)
elif figura=="rectangulo":
    print("las dimensiones no son correctas , pero los espacios estan bien")
    print("se sugieren medidas mayores al 1 en el primer lado")
    b = int(input("dame el primer lado del rectangulo: "))
    b2 = int(input("cual es el otro lado: "))
    contador=b
    contador2=0
    b2-=2
    for i in range (b-1):
        a="┎"
        m="┒"
        c="|"
        d=" " 
        j="─"
        k="┖"
        o="┚"
        if contador == b:
            print(a+j*b2+m)
            contador-=1
            i+=1
        if contador == 1:
            print(k+j*b2+o)
            i+=1
        elif contador > 0:
            print(c+d*b2+c)
            contador-=1
            i+=1
elif figura=="circulo":
    print("""             .adAHHHAbn.                     
            dHHHHHHHHHHHb                     
           dHHHHHHHHHHHHHb                   
           HHHHHHHHHHHHHHH                  
           VHHHHHHHHHHHHHP                 
            YHHHHHHHHHHHP              
             "^YUHHHUP^""")
    b=int(input("escoge el radio y sera dibujado por una tortuga: "))
    turtle.shape("turtle")
    turtle.setup(640, 480, 0, 0)
    turtle.circle(b)
    turtle.mainloop()
print("fin del programa,gracias por utilizarlo")
