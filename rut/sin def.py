list = []
n=8
ResSuma=0
while 0 < n:
    rut = int(input("introduce los numeros de su rut en orden uno x uno"))
    list.append(rut)
    ResSuma=rut+ResSuma
    a = rut
    n -= 1

if (11-((list[0]*3+list[1]*2+list[2]*7+list[3]*6+list[4]*5+list[5]*4+list[6]*3+list[7]*2)%11))>0 and (11-((list[0]*3+list[1]*2+list[2]*7+list[3]*6+list[4]*5+list[5]*4+list[6]*3+list[7]*2)%11)) <10:
    print("el digito verificador de su rut es",(11-((list[0]*3+list[1]*2+list[2]*7+list[3]*6+list[4]*5+list[5]*4+list[6]*3+list[7]*2)%11)))
elif (11-((list[0]*3+list[1]*2+list[2]*7+list[3]*6+list[4]*5+list[5]*4+list[6]*3+list[7]*2)%11))== 11:
    print("el codigo verificador de su rut es 0")
else:
    print("el codigo verificador de su rut es K" )





    



