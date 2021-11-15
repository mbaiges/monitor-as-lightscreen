from tkinter import *
import random
import math

root = Tk()

screen_width = 1920
screen_height = 1080
canvas = None
canvas_width = screen_width
canvas_height = screen_height

color_idx = 0

predefined_colors = {
    'white': {
        'hex': '#FFFFFF'
    },
    'pink': {
        'hex': '#F8B5FF'
    }
}

def init():
    global canvas, canvas_width, canvas_height, screen_width, screen_height

    canvas_width = screen_width
    canvas_height = screen_height

    canvas = Canvas(root, 
            width=canvas_width,
            height=canvas_height)
    canvas.pack()

    update(None)

def update(event):
    global canvas, canvas_width, canvas_height, screen_width, screen_height, color_idx

    c = "#FFFFFF"

    if event is not None or hasattr(event, 'char'):
        char = event.char

        hex_colors = list(map(lambda o: o['hex'], predefined_colors.values()))

        if char == 'a':
            color_idx = color_idx - 1 if color_idx > 0 else color_idx
            c = hex_colors[color_idx]
        elif char == 'd':
            color_idx = color_idx + 1 if color_idx < (len(hex_colors)-1) else color_idx
            c = hex_colors[color_idx]
        elif char == 'r':
            r = random.randint(0, math.pow(2, 24))
            c = str(hex(r)).replace('0x', '#')

    canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill=c)

    root.bind("<Key>", update)

init()

mainloop()