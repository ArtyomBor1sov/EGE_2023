from turtle import *

k = 40
color('black', 'red')
speed(0)
begin_fill()
for i in range(4):
    forward(10 * k)
    right(90)
end_fill()
right(30)
color('black', 'green')
begin_fill()
for i in range(2):
    forward(6 * k)
    right(60)
    forward(6 * k)
    right(120)
end_fill()
canvas = getcanvas()
counter = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        s = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if len(s) == 1 and s[0] == 5:
            counter += 1
print(counter)
done()