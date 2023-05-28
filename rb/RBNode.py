class RBNode:
    RED = "r"
    BLACK = "b"
    def __init__(self, data, color=RED):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
        