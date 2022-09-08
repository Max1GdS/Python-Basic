print("este programa sirve para crear una fecha con 3 valores")
año =int (input("escribe un año valido entre 1-2021: "))
mes=int(input("escribe un mes valido entre el 1-12: "))
dia=int(input("escribe un dia valido: "))
if año > 0 and año <= 2021 and mes > 0 and mes <= 12:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 0 and dia <=31:
            print("la fecha es valida")
        else:
            print("la fecha no es valida")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 0 and dia <= 30:
            print("la fecha es valida")
        else:
            print("la fecha no es valida")
    elif año % 4 == 0 and año % 100 !=0:
        if mes == 2:
            if dia > 0 and dia <= 29:
                print("la fecha es valida")
            else:
                print("la fecha no es valida")
        else:
            print("la fecha no es valida")
    elif año % 4 == 0 and año % 100 ==0 and año % 400 == 0:
        if mes == 2:
            if dia > 0 and dia <= 29:
                print("la fecha es valida")
            else:
                print("la fecha no es valida")
    elif año > 0 and año <= 2021:
        if mes==2 and dia > 0 and dia <= 28:
            print("la fecha es valida")
        else:
            print("la fecha no es valida")
    else:
        print("la fecha no es valida")
else:
    print("la fecha no es valida")


        


