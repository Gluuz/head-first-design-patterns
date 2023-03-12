from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass
    