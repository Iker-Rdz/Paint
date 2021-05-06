from turtle import *
from freegames import vector
#Se insertan las librerías necesarias
def line(start, end):
    "Draw line from start to end."
    up() #Levanta la pluma
    goto(start.x, start.y) #Posicion x,y
    down() #Bajar la pluma y dibujar
    goto(end.x, end.y) #Posición x,y

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4): #Trazar 4 lineas
        forward(end.x - start.x)
        left(90) #Rotar 90 grados

    end_fill()
#Se define la función para hacer el cuadrado
def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    radi = (end.x - start.x)/2 #se define el radio
    diam = end.x - start.x #se define el diametro
    cx = 0
    cy = 0 #Se definen los cambios en "x" y "y"
    for count in range(0, diam + 1, 0.5): #se crea un ciclo que abarca toda la trayectoria de la media circunferencia superior
	cx = count #se le asigna al cambio en x el valor del contador
	cy = (radi - (cx ** 2)) ** 0.5 #se asigna el valor del cambio en y con base en la fórmula del círculo
	goto(start.x + cx, start.y + cy) #se hace el desplazamiento a por la media circunferencia
    for count in range(0, diam + 1, 0.5): #se repite el proceso pero para la media circunferencia inferior
	cx = count
	cy = (radi - (cx ** 2)) ** 0.5
	goto(end.x - cx, end.y - cy) #aquí está el cambio, en vez de empezar en el inicio se va al final, y los cambios son negativos
    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('violet'), 'V') #este es el color agregado
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
