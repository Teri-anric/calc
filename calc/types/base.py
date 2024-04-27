from abc import ABCMeta, abstractmethod
from typing import Optional


class BaseExpr(metaclass=ABCMeta):
    @abstractmethod
    def eval(self, data: dict):
        raise NotImplementedError("Must implement this method")


class VoidExpr(BaseExpr):
    def eval(self, data: dict):
        return 0

    def __str__(self):
        return " "


class BaseOperation(BaseExpr, metaclass=ABCMeta):
    a: Optional[BaseExpr]
    b: Optional[BaseExpr]
    OPERATOR: str = "?"

    def __init__(self, a, b):
        if not isinstance(a, BaseExpr):
            raise TypeError("Left operands must be of type BaseExpr")
        if not isinstance(b, BaseExpr):
            raise TypeError("Right operands must be of type BaseExpr")
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a} {self.OPERATOR} {self.b})"


class BaseNum(BaseExpr, metaclass=ABCMeta):
    def __init__(self, string: str):
        self.string = string.strip()

    def __str__(self):
        return self.string
