from pizza_store import PizzaStore
from chicago_style_cheese_pizza import ChicagoStyleCheesePizza
from chicago_style_pepperoni_pizza import ChicagoStylePepperoniPizza
from pizza import Pizza

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, type: str) -> Pizza or None:
        if type == "cheese":
            return ChicagoStyleCheesePizza()
        elif type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None