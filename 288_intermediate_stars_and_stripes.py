"""
https://redd.it/589txl

Description

This challenge is about drawing stars. Specifically, each point should be
equally spaced to the ones beside it, and should be connected to the two
opposite points with a line. Not the direct opposite though, like when you have
an even number of points. For example, take a look at this image.

In the first star, the pentagram with an odd amount of points, it's clear what 
"connected to the two opposite points" means. In the hexagram it's not just as 
clear. That's why the image shows that exactly opposite points should not be 
connected. Formal Inputs and Outputs

Input
You will be given the amount of vertices, or points in the specific star.

Output
The output should be any type of image with the star rendered onto it.

Challenge input

8 7 20

Bonus challenge

Surround the star by a polygon with the same amount of vertices. For example, if
the input is 5, the output should be a pentagram (5-pointed star) surrounded by
a pentagon. Tips

If you want to find a point's coordinates from only a distance and angle, here's
how to do that: x = d cos a y = d sin a Remember that many languages measure in
radians! To convert from degrees to radians, multiply by pi/180. If you want to
find the relationship to pi, just divide by 180. For example, 360/180 is 2, so
360 is 2pi rad. Also, wolfram alpha is really useful for simplifying math 
expressions quickly.
"""
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
