from abc import ABCMeta, abstractmethod

class BaseExpr(metaclass=ABCMeta):
    @abstractmethod
    def eval(self,  **kwargs):
        raise NotImplementedError("Must implement this method")