import abc


class AbsFactory(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def create_saver():
        pass

    @staticmethod
    @abc.abstractmethod
    def create_investor():
        pass
