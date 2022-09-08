#Por medio de pseudocódigo y Diagrama de flujo, realizar:
#1.- Realizar un algoritmo que solicite la hora, los minutos 
#y segundos. Posteriormente, muestre el equivalente en segundos, 
#el equivalente en minutos, y el equivalente en horas. (10 pts)

print("este programa realizara un calculo que cambiara el tiempo en segundo y minutos")
a = int(input("dame las horas: "))
b = int(input("dame los minutos: "))
c = int(input("dame los segundos: "))

resseg = a * 3600 + b * 60 + c 
resmin= a * 60 + b + (c/60)
reshora= a + (b / 60) + (c/3600)

print("el tiempo en segundos es: ",str(resseg))
print("el tiempo en minutos es: ",str(resmin))
print("el tiempo en hora es: ",str(reshora))

