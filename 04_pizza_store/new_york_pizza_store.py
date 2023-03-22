from pizza_store import PizzaStore
from new_york_style_cheese_pizza import NYStyleCheesePizza
from new_york_style_pepperoni_pizza import NYStylePepperoniPizza
from pizza import Pizza


class NYPizzaStore(PizzaStore):
    def createPizza(self, type: str) -> Pizza or None:
        if type == "cheese":
            return NYStyleCheesePizza()
        elif type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None
