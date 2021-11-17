from tkinter import *

from models.Context import Context
from models.commands.SwitchPlainColorCommand import Direction, SwitchPlainColorCommand
from models.commands.RandomPlainColorCommand import RandomPlainColorCommand

tk = Tk()
canvas = None
width = 1920
height = 1080
vars = {}

ctx = Context(tk, canvas, width, height)

def init():
    global ctx

    canvas_width = ctx.width
    canvas_height = ctx.height

    ctx.canvas = Canvas(ctx.tk, 
            width=canvas_width,
            height=canvas_height)
    ctx.canvas.pack()

    ctx.tk.bind("<Key>", key_handler)
    ctx.tk.bind("<Left>", lambda event: SwitchPlainColorCommand().with_arguments({'direction': Direction.LEFT}).with_context(ctx).execute())
    ctx.tk.bind("<Right>", lambda event: SwitchPlainColorCommand().with_arguments({'direction': Direction.RIGHT}).with_context(ctx).execute())

def key_handler(event):
    global ctx

    cmd = None

    if event is not None or hasattr(event, 'char'):
        char = event.char

        if char == 'a':
            cmd = SwitchPlainColorCommand().with_arguments({'direction': Direction.LEFT})
        elif char == 'd':
            cmd = SwitchPlainColorCommand().with_arguments({'direction': Direction.RIGHT})
        elif char == 'r':
            cmd = RandomPlainColorCommand()

    if cmd is not None:
        cmd.with_context(ctx).execute()

init()

mainloop()