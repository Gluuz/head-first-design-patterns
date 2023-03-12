from beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "DarkRoast"

    def cost(self):
        return 0.99
    