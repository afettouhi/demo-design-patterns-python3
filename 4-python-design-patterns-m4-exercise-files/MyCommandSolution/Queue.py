from actions.order import Order
from command_abc import AbsCommand


class LifoQueue(AbsCommand):
    def __init__(self, order):
        if not isinstance(order, Order):
            raise TypeError
        self.order = order

    def put(self):
        self.order.get()

    def undo(self):
        self.order.empty()

    def execute(self):
        pass
