from abc import abstractmethod

from beverage import Beverage


class CondimentDecorator(Beverage):
    def cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass 