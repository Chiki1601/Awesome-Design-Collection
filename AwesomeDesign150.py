# Awesome Design 150 in Python
from turtle import *
import colorsys
bgcolor("black")
pensize(5)
speed(0)
h = 0

for i in range(150):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    color(c)
    h +=0.05
    up()
    goto(0,0)
    fd(i)
    down()
    circle(i)
    lt(181)
    fd(300)
    rt(154)
ht()
done()
