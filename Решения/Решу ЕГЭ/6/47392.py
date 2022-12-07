from turtle import *

k = 40
color('black', 'red')
speed(0)
begin_fill()
for i in range(6):
    forward(10 * k)
    right(60)
end_fill()
canvas = getcanvas()
counter = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if len(s) > 0:
            counter += 1
print(counter)
done()