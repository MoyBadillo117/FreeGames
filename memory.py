"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

 Brandon Saavedra Cortes a01748300
 Moises Badillo Cruz a00834306
"""
#Moisés Arturo Badillo Álvarez (A00834306)
#Brandon Kevin Saavedra Cortés (A01748300)

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = ["A","B","Γ","Δ","E","Z","H","Θ","I","K","Λ","M","N","Ξ","O","Π","P","Σ","T","Y","Φ","X","Ψ","Ω","a","β","y","δ","ε","ζ","η","θ"]*2 #Cambio los numeros por letras para que sea más fácil de recordar y para poder centrarlos mejor
state = {'mark': None}
hide = [True] * 64
contaps = 0 #Variable donde se almacenara el número de taps
puntos = 0 #Variable donde se almacenara el número de puntos

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        global contaps 
        contaps +=1 #Cada vez que se hace tap se agrega al contador
        print(contaps) #Se imprime en consola el número de taps 
        #write(contaps, font=('Arial', 30, 'normal')) #Se elimina codigó innecesario que afecta el desarrollo

    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global puntos
        puntos += 1
        print(contaps) 
        if puntos == 32: #Se verifica que el contador de puntos ya sea 32 para así desmostrar que el juego ha finalizado
            print("Has ganado") #Cuando se finaliza el juego imprime que ha ganado el usuario
        up()
        goto(0, 600)
        color('black')
        write(puntos, font=('Arial', 30, 'normal'))

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 9, y-5) #Centro las letras
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
