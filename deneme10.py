from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

width(10)


def draw_rectangle(linecolor, length1=100, length2=150):
    color(linecolor)
    for i in range(2):
        forward(length1)
        left(90)
        forward(length2)
        left(90)


draw_rectangle('blue')

done()
