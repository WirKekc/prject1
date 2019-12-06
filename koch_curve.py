import turtle

# my_turtle = turtle.Turtle()
# window = turtle.Screen()
# num = int(input())


def koch(n, a=[]):
    if n > 0:
        n -= 1
        koch(n)
        a.append(60)
        koch(n)
        a.append(-120)
        koch(n)
        a.append(60)
        koch(n)
    return a


def turtle_koch_curve(n, speed, sw, sh):
    window = turtle.Screen()  # создали окно
    window.title('Koch curve')  # назвали
    # window.screensize(sw, sh)  # задали размер

    mikey = turtle.Turtle()  # создали черепаху
    mikey.screen.setup(sw, sh)
    mikey.speed(speed)  # скорость
    mikey.up()
    mikey.setpos(-sw // 2, -sh // 2)  # позиция
    mikey.down()

    # посчитали необходимую длину линии
    length = sw * 3//10
    for _ in range(n - 1):
        length /= 3

    for move in koch(n):
        mikey.forward(length)
        mikey.left(move)
    mikey.forward(length)

    window.exitonclick()


num = int(input('Deep of Koch: '))
sp = int(input('Speed of drawing: '))
width = int(input('Width of window: '))
height = int(input('Height of window: '))

turtle_koch_curve(num, sp, width, height)  # запускаем функцию