import time
import turtle
print('Bienvenido, este programa le dibujara una figura geometrica que ud especifique')
print('para ello tiene 2 alternativas:')
time.sleep(1)
print('ocupar ascii u ocupar turtle')

eleccion=input('digite "ascii" o "turtle" :')
if eleccion == 'ascii':
    print('usted a elegido ascii')
    figura=input('escriba a continuacion que figura quiere que se dibuje (OPCIONES circulo \ rectangulo \ triangulo) :')
    if figura=='circulo':
        print('|         ***     \n|       *     *   \n|      *       *  \n|                 \n|     *         * \n|     *         * \n|     *         * \n|                 \n|      *       *  \n|       *     *   \n|         ***   ')
    elif figura=='rectangulo':
        print('|---------------------|\n|                     |\n|                     |\n|                     |\n|---------------------|')
    elif figura=='triangulo':
        print('                        /\ \n                      /    \ \n                    /        \ \n                  /            \ \n                /                \ \n              /                    \ \n            /                        \ \n          /                            \ \n        /                                \ \n       /__________________________________\ ') 
elif eleccion == 'turtle':
    print('usted a elegido turtle')
    figura=input('escriba a continuacion que figura quiere que se dibuje (OPCIONES circulo \ rectangulo \ triangulo) :')
    if figura=='circulo':
        turtle.setup(640, 480, 0, 0)
        vantana = turtle.getscreen()
        a = turtle.Turtle()
        a.pencolor('red')
        a.begin_fill()
        
        a.circle(100)

        a.color('red')
        a.fillcolor('red')
        a.end_fill()

        turtle.done()
    elif figura =='rectangulo':
        turtle.setup(640, 480, 0, 0)
        vantana = turtle.getscreen()
        a = turtle.Turtle()
        a.pencolor('red')
        a.begin_fill()
        a.forward(250) # base
 
        a.left(90)
        a.forward(150) # lado der
 
        a.left(90)
        a.forward(250) #cielo
        
        a.left(90)
        a.forward(150) # lado izq
        
        a.color('red')
        a.fillcolor('red')
        a.end_fill()

        turtle.done()
    elif figura =='triangulo':

        turtle.setup(640, 480, 0, 0)
        vantana = turtle.getscreen()
        a = turtle.Turtle()
        a.pencolor('red')
        a.begin_fill()
        a.forward(200) # draw base
 
        a.left(120)
        a.forward(200)
 
        a.left(120)
        a.forward(200)
        a.color('red')
        a.fillcolor('red')
        a.end_fill()

        turtle.done()
time.sleep(5)
print('FIN DEL PROGRAMA')