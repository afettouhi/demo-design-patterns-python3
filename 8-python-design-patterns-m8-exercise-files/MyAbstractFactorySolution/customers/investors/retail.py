from ..abs_customers import AbsCustomers


class Retail(AbsCustomers):
    def report_type(self):
        print('"%s" is a retail investor.' % self.name)
