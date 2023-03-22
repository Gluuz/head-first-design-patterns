from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def prepare(self):
        # the abstract class provides some basics defaults for baking,
        # cutting and boxing
        # preparation follows a number of steps in a particular sequence
        print("Preparing", self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for topping in self.toppings:
            print("    " + topping)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def getName(self):
        return self.name
