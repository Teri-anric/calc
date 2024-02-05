import math
from abc import ABCMeta
from fractions import Fraction

from calc.parse import parse_expression

from .base import BaseExpr

to_num = Fraction


class BaseNum(BaseExpr, metaclass=ABCMeta):
    def __init__(self, string: str):
        self.string = string.strip()

    def __str__(self):
        return self.string


class Num(BaseNum):
    def eval(self, **kwargs):
        return to_num(self.string)


class ConstNum(BaseNum):
    def eval(self, **kwargs):
        return to_num(kwargs[self.string])


class PiNum(BaseNum):
    def eval(self, **kwargs):
        return to_num(math.pi)


class FuncNum(BaseNum):
    def __init__(self, string: str):
        super().__init__(string)
        name, _, q = string.partition('(')
        self.name = name.strip()
        self.expression = parse_expression("(" + q)

    def eval(self, **kwargs):
        return to_num(kwargs[self.name](
            self.expression.eval()
        ))


class SqrtNum(BaseNum):
    def __init__(self, string: str):
        super().__init__(string)
        a, _, b = string.partition('√')
        if not a.isdigit():
            a = 1
        self.a = int(a)
        self.b = parse_expression(b)

    def eval(self, **kwargs):
        return to_num(
            float(self.b.eval() * (self.a ** 2)) ** 0.5
        )
