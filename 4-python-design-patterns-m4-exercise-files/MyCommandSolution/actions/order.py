class Order(object):
    def __init__(self, name):
        self.name = name

    def empty(self):
        print("%s is emptied." % self.name)

    def get(self):
        print("%s is completed." % self.name)
