from condiment_decorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()