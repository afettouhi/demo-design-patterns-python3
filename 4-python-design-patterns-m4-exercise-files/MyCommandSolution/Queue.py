from actions.order import SetOrder
from command_abc import AbsCommand


class LifoQueue(AbsCommand):
    def __init__(self, order):
        if not isinstance(order, SetOrder):
            raise TypeError('Expected a Door object, got %s instead.' % order.__class__.__name__)
        self.order = order

    def put(self):
        self.order.get()

    def undo(self):
        self.order.empty()
