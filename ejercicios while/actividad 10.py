print("este programa te ayudar a saber la serie de fubonacci")
n = int(input("cuantos numeros quieres de la serie: "))
a=0
b=1
c=0
for i in range (n):
    c=a+b
    print(str(a), end=(" ")) 
    a = b
    b = c
print()
print("gracias por utilizar este programa")