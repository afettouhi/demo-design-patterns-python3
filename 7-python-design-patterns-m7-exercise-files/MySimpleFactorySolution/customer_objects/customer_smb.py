from .abs_customer import AbsCustomer


class CustomerSmb(AbsCustomer):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def send_invoice(self):
        print('Sending invoice to SMB customer "%s".' % self._name)
