from abs_builder import AbsBuilder


class MyPizzaMaker(AbsBuilder):

    def make_crust(self):
        self._pizza.crust = 'Whole wheat, thin'
     
    def add_sauce(self):
        self._pizza.base = 'Tomato sauce'

    def add_meat(self):
        self._pizza.meat_toppings = 'Pepperoni & sausage'

    def add_vegetables(self):
        self._pizza.vegetable_toppings = 'Onions & peppers'

    def add_cheese(self):
        self._pizza.cheese_toppings = 'Quattro formaggi'
