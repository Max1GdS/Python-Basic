#huevos fritos y arroz
print ('hola, este programa sirve para aprender a hacer arroz blanco y huevo frito')
print ('escriba 1 si quiere la receta de arroz blanco')
print ('escriba 2 si quiere la receta del huevo frito')
a = int (input("ingresa la opción que quieres cocinar : "))
if a == 2:
    print ('usted a elegido la receta de huevo frito')
    b = int (input ('cuantos huevos fritos hará?'))
    hvs = b
    sal = 2
    hvssal = sal * b
    print ('busque una sarten de un tamano en proporcion a los huevos que va a hacer, limpia y en buen estado. agregar ', hvs ,' cucharadita de aceite vegetal,')
    print ('y esperar medio minuto a fuego alto para se que se caliente el aceite')
    print ('bajar el fuego a medio y agrega el/los huevo/s que desea cocinar, y agregue ',hvssal,' gramos de sal. Espere aprox 1 y medio')
    print ('apague y sirva')
if a == 1:
    print ('usted a elegido la receta de arroz blanco')
    print ('Busque una olla de un tamano en proporcion a las personas que comeran, y en buen estado')
    d = int (input ('ingrese el numero de personas que comeran'))
    arroz = 1
    agua = 2
    sal = 4
    ace = 2
    arrozper = d * arroz
    aguaper = d * agua
    salper = d * sal
    aceper = d * ace
    print ('Agregar ',arrozper,' taza de arroz blanco, ',aguaper,' tazas de agua, ',salper,' gramos de sal y ',aceper,' gramos de aceite vegetal,')
    print ('todo de una vez. Revuelve un poco sólo en una oportunidad.')
    print ('Pon a fuego alto y deja que hierva durante unos 10 a 15 minutos aproximadamente.')
    print ('apaga el fuego y sirva de inmediato')
print ('Fin de la receta.')
