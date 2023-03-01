from turtle import *

k = 40
speed(0)
left(90)
color('black', 'red')
begin_fill()
for i in range(6):
    forward(5 * k)
    right(60)
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