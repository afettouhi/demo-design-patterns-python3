from abs_builder import AbsBuilder


class CustomerPizzaMaker(AbsBuilder):

    def make_crust(self):
        self._pizza.crust = 'Regular'

    def add_sauce(self):
        self._pizza.base = 'Tomato sauce'

    def add_meat(self):
        self._pizza.meat_toppings = 'Sausage & bacon'

    def add_vegetables(self):
        self._pizza.vegetable_toppings = 'Tomatoes, onions & peppers'

    def add_cheese(self):
        self._pizza.cheese_toppings = 'Provolone'
