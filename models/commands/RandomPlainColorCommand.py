import random
import math

from models.commands.Command import *

class RandomPlainColorCommand(Command):

    def execute(self):
        super().execute()

        canvas = self.ctx.canvas

        r = random.randint(0, math.pow(2, 24))
        c = str(hex(r)).replace('0x', '#')

        canvas.create_rectangle(0, 0, self.ctx.width, self.ctx.height, fill=c)