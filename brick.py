import math
from cadquery import func as cf

def clutch_brick(rows, cols, height, stud_d, stud_h, spacing):
    length = cols * spacing - 0.4
    width = rows * spacing - 0.2
    body = cf.box(length, width, height)
    stud = cf.cylinder(d=stud_d, h=stud_h)

    for r in range(rows):
        for c in range(cols):
            x_pos = (c - (cols - 1) / 2) * spacing
            y_pos = (r - (rows - 1) / 2) * spacing
            body = body + stud.moved(x=x_pos, y=y_pos, z=height)

    return body

rows, cols = 2, 4
height, stud_d, stud_h, spacing = 9.6, 4.8, 1.7, 8.0

brick = clutch_brick(rows, cols, height, stud_d, stud_h, spacing)

length = cols * spacing - 0.4
width = rows * spacing - 0.2
num_studs = rows * cols
expected = (length * width * height) + num_studs * (math.pi * (stud_d / 2) ** 2 * stud_h)

assert abs(brick.Volume() - expected) < 0.5
print("Valid:", brick.isValid(), "Volume:", round(brick.Volume(), 1))
brick.exportStl("brick.stl")
