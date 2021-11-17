from models.commands.Command import *

from enum import Enum
class Direction(Enum):
    LEFT = -1
    RIGHT = 1

predefined_colors = {
    'white': {
        'hex': '#FFFFFF'
    },
    'pink': {
        'hex': '#F8B5FF'
    }
}

hex_colors = list(map(lambda o: o['hex'], predefined_colors.values()))

class SwitchPlainColorCommand(Command):

    def __init__(self):
        self._prefix = "spc"

    def execute(self):
        super().execute()

        canvas = self.ctx.canvas
        color_idx = self.ctx.vars[self.prefixed('color_idx')] if self.prefixed('color_idx') in self.ctx.vars else 0
        direction = self.args['direction']

        if direction == Direction.LEFT:
            color_idx = color_idx - 1 if color_idx > 0 else color_idx
            c = hex_colors[color_idx]
        elif direction == Direction.RIGHT:
            color_idx = color_idx + 1 if color_idx < (len(hex_colors)-1) else color_idx
            c = hex_colors[color_idx]

        self.ctx.vars[self.prefixed('color_idx')] = color_idx

        canvas.create_rectangle(0, 0, self.ctx.width, self.ctx.height, fill=c)