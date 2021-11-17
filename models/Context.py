class Context:
    
    def __init__(self, tk, canvas, width, height, vars = {}):
        self.tk = tk
        self.canvas = canvas
        self.width = width
        self.height = height
        self.vars = vars