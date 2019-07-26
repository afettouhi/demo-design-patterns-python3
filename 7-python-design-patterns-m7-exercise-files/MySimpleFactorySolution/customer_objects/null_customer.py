from .abs_customer import AbsCustomer


class NullCustomer(AbsCustomer):
    def __init__(self, customer_type):
        self._customer_type = customer_type

    @property
    def name(self):
        return None

    @name.setter
    def name(self, name):
        pass

    def send_invoice(self):
        print('Customer of "%s" type found.' % self._customer_type)
