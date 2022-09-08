print ('hola, este programa hara una una sentencia con el concepto (^2,*2,-2)\n\n')
largo= int(input('cuan largo quiere que sea la sentencia , Escriba un numero(numeros muy pequeÃ±os por favor xD): '))
if largo > 0 :
    #implementacion de lisa para saber la suma de la sentencia
    lista=[]
    base= int(input("en base a que numero quiere que se desarrolle la sentencia?: "))
    lista.append (base)
    for i in range(largo):
        #potencia
        lista.append (base ** 2)
        base= base ** 2 
        #multiplo
        lista.append (base * 2)
        base= base * 2
        #resta
        lista.append (base - 2)
        base= base - 2
    #resultados por terminal
    print (lista)
    #suma de resultados
    print ("La suma de la sentencia es: ",sum(lista) )
#if numero es invalido (el numero de veces que se repetira no puede ser negativo)
else:
	print ("el numero ingresado no es valido intente nuevamente")

#no supe separar los resultados, es decir que si introduce que se repitaa 10 veces le mostrara 30 resultados porque las operaciones estan juntas. :frowning:

