from new_york_pizza_store import NYPizzaStore
from chicago_pizza_store import ChicagoPizzaStore


if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza("cheese")
    print("Ethan ordered a " + pizza.getName() + "\n")

    pizza = chicagoStore.orderPizza("cheese")
    print("Joel ordered a " + pizza.getName() + "\n")
