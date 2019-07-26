from ..abs_customers import AbsCustomers


class Government(AbsCustomers):
    def report_type(self):
        print('"%s" is a government saver.' % self.name)
