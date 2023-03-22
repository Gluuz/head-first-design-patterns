from pizza import Pizza


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Pepperoni Pizza"
        self.dough = "Dough"
        self.sauce = "Pomodoro Sauce"

        self.toppings.append("Pecorino Cheese")