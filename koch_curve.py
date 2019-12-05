# import turtle
num = int(input())


def koch(n):
    a = []
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

# def turtle_koch_curve(n, line_length=10):
#     for move in koch(n):
#         turtle.forward(line_length)
#         turtle.left(move)
#     turtle.forward(line_length)
#
#
# turtle_koch_curve(num)

print(koch(num))