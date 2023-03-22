from pizza import Pizza


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Pepperoni Pizza"
        self.dough = "Dough"
        self.sauce = "Margherita Sauce"

        self.toppings.append("Mozzarella Cheese")