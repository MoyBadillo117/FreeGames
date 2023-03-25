"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

# Brandon Saavedra Cortes a01748300
 Moises Badillo Cruz a00834306

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colores = ['black','orange', 'purple', 'green','blue','gray']
ran = random.choice(colores)
colorComida = ran
colores.remove(ran)
colorSerpiente = random.choice(colores)

def change(x, y):
# Cambio en el movimiento de la serpiente
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global food
#se desplaza una casilla o un espacio dentro del tablero o area de juego
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
#Se cambia tamaño de la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSerpiente)

    coordenada = [vector(10, 0), vector(-10, 0), vector(0, -10), vector(0, 10)]
    posicion = random.choice(coordenada)
    if randrange(10) == 0:
        if inside(food + posicion):
            food += posicion
    square(food.x, food.y, 9, colorComida)
    update()
    ontimer(move, 60)
# se cambia aparición de la serpiente o Respawn
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
