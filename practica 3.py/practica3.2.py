#Dada una variable c que contiene un carácter, escribe las expresiones que representen las siguientes afirmaciones:
#a) c es una vocal.
#b) c es una letra minúscula.
#c) c es un símbolo del alfabeto.
c = str(input("introduce una letra: "))
if c=="a" or c=="e" or c=="i" or c=="o" or c=="u" or c=="A" or c=="E" or c=="I" or c=="O" or c=="U":
    print("la variable c es una vocal")
else:
    print("la variable c no es una vocal")
if c=="q" or c=="w" or c=="e" or c=="r" or c=="t" or c=="y" or c=="u" or c=="i" or c=="o" or c=="p" or c=="a" or c=="s" or c=="d" or c=="f" or c=="g" or c=="h" or c=="j" or c=="k" or c=="l" or c=="ñ" or c=="z" or c=="x" or c=="c" or c=="v" or c=="b" or c=="n" or c=="m":
    print("la variable c es minuscula")
if c=="Q" or c=="W" or c=="E" or c=="R" or c=="T" or c=="Y" or c=="U" or c=="I" or c=="O" or c=="P" or c=="A" or c=="S" or c=="D" or c=="F" or c=="G" or c=="H" or c=="J" or c=="K" or c=="L" or c=="Ñ" or c=="Z" or c=="X" or c=="C" or c=="V" or c=="B" or c=="N" or c=="M":
    print("la variable c es mayuscula")
else:
    print("es un simbolo del alfabeto")





