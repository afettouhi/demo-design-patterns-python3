from .abs_customer import AbsCustomer


class CustomerEnt(AbsCustomer):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def send_invoice(self):
        print('Sending invoice to ENT customer "%s".' % self._name)
