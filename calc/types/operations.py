from abc import ABCMeta
from typing import Optional

from .base import BaseExpr
from calc.parse.parse_expr import parse_expression


class BaseOperation(BaseExpr, metaclass=ABCMeta):
    a: Optional[BaseExpr]
    b: Optional[BaseExpr]
    OPERATOR: str = "?"

    def __init__(self, a, b):
        if isinstance(a, str):
            a = parse_expression(a)
        self.a = a
        if isinstance(b, str):
            b = parse_expression(b)
        self.b = b

    def __str__(self):
        return f"({self.a} {self.OPERATOR} {self.b})"


class AddOperation(BaseOperation):
    OPERATOR = "+"

    def eval(self, **kwargs):
        return (
                self.a.eval(**kwargs)
                + self.b.eval(**kwargs)
        )


class MulOperation(BaseOperation):
    OPERATOR = "*"

    def eval(self, **kwargs):
        return (
                self.a.eval(**kwargs)
                * self.b.eval(**kwargs)
        )


class SubOperation(BaseOperation):
    OPERATOR = "-"

    def eval(self, **kwargs):
        return (
                self.a.eval(**kwargs)
                - self.b.eval(**kwargs)
        )


class DivOperation(BaseOperation):
    OPERATOR = "/"

    def eval(self, **kwargs):
        return (
                self.a.eval(**kwargs)
                / self.b.eval(**kwargs)
        )


class PowOperation(BaseOperation):
    OPERATOR = "^"

    def eval(self, **kwargs):
        return (
                self.a.eval(**kwargs)
                ** self.b.eval(**kwargs)
        )


class NotOperation(BaseOperation):
    OPERATOR = "~"

    def eval(self, **kwargs):
        return (self.a.eval(**kwargs)
                - self.b.eval(**kwargs)
                ) ** 2


OPERATIONS_CLASS = {
    "~": NotOperation,
    "^": PowOperation,
    "/": DivOperation,
    "*": MulOperation,
    "-": SubOperation,
    "+": AddOperation
}
OPERATIONS = list(OPERATIONS_CLASS.keys())
