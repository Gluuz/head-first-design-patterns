from condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()