print('Pruebas de formatos de impresión')
print('--------------------------------\n')
# Inicializamos las variables
dato1 = 205
dato2 = 205.5
dato3 = 'hola'
# Pruebas
print('Entero en bases 10 y 16 : %d %x' % (dato1 , dato1))
print('Entero alineado derecha (6 pos rell 0) : %06i' % (dato1))
print('Real sin formato : %f' % (dato2))
print('Real con dos decimales : %.2f' % (dato2))
print('Real alineado derecha (12 pos 0 decim) : %12.0f' % (dato2))
print('Real alineado derecha (12 pos 2 decim) : %12.2f' % (dato2))
print('Real con formato exponencial : %e' % (dato2))
print('Cadena alin. izquierda (20 pos) : %20s' % (dato3))
print('Cadena alin. derecha (20 pos) : %-20s' % (dato3))
