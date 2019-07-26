from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .null_customer import NullCustomer
from .abs_customer import AbsCustomer


def load_customer(customer_type):
    try:
        customer_module = import_module('.' + customer_type, 'cust_objects')
    except ImportError:
        return NullCustomer(customer_type)

    classes = getmembers(customer_module,
                         lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, AbsCustomer):
            return _class()
