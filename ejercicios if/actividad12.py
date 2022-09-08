print("este es un programa que calcula el gasto de agua en una vivienda dado el número de litros gastados")
a = float(input("cuantos litros ha gastado : "))
if a <= 50:
    print("tendría que pagar solamente los 6 dólares de la cuota fija mensual")
elif a > 50 and a < 200:
    b = 6 +(a-50)*0.1
    print("tendría que pagar solamente "+ str(round(b,2)) +" dólares")
elif a <= 0:
    print ("no tiene litros o el numero no es valido")
else:
    c=6+(a-50)*0.1+(a-200)*0.3
    print("tendria que pagar solamente "+ str(round(c,2)) +" dolares")
print("gracias por utilizar este programa")