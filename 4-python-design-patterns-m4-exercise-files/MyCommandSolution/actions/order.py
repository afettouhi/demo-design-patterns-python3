class SetOrder(object):
    def __init__(self, name):
        self.name = name

    def empty(self):
        print("%s is locked." % self.name)

    def get(self):
        print("%s is locked." % self.name)
