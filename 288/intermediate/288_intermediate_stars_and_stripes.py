import turtle


def draw_outline(poly, n, length = 50, color = 'red', speed = 5):
    poly.color(color)
    poly.speed(speed)
    for i in range(n):
        poly.forward(length)
        poly.left(360.0 / n) 


def draw_star(poly, n, skip, color = 'blue', speed = 5):
    poly.color(color)
    poly.speed(speed)
    v = 0
    verts = poly.get_poly()
    for i in range(n):
        v = v + skip
        if v >= n:
            v = v - n
            poly.goto(verts[v])
        else:
            poly.goto(verts[v])


def draw_poly(n):
    m = (n / 2 - 1) if (n % 2 == 0) else n / 2
    draw_outline(polygon, n)
    draw_star(polygon, n, m)


window = turtle.Screen()
polygon = turtle.Turtle()
polygon.begin_poly()

draw_poly(8)

window.exitonclick()
