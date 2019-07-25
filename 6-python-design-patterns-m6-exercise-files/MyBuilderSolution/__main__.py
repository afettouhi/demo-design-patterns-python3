from pizza_maker import PizzaMaker
from my_pizza_maker import MyPizzaMaker
from customer_pizza_maker import CustomerPizzaMaker

pizza_builder = PizzaMaker(MyPizzaMaker())
pizza_builder.make_pizza()
pizza = pizza_builder.get_pizza()
pizza.display()

pizza_builder = PizzaMaker(CustomerPizzaMaker())
pizza_builder.make_pizza()
pizza = pizza_builder.get_pizza()
pizza.display()
