from ..abs_customers import AbsCustomers


class Commercial(AbsCustomers):
    def report_type(self):
        print('"%s" is a commercial investor.' % self.name)
