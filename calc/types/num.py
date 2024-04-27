import math
from fractions import Fraction

from .base import BaseExpr, BaseNum

to_num = Fraction

__all__ = ['Num', 'ConstNum', 'PiNum', 'FuncNum', 'SqrtNum', 'FunctionNum', 'StrNum']


class Num(BaseNum):
    def eval(self, data):
        return to_num(self.string)


class ConstNum(BaseNum):
    def eval(self, data):
        return to_num(data[self.string])


class PiNum(BaseNum):
    def eval(self, data):
        return to_num(math.pi)


class FuncNum(BaseNum):
    def __init__(self, string: str, name: str, expr: BaseExpr):
        super().__init__(string)
        self.name = name.strip()
        self.expression = expr

    def eval(self, data: dict):
        local_data = data.copy()
        self.expression.eval(local_data)
        return to_num(data[self.name](
            local_data
        ))

    def __str__(self):
        return f'{self.name}({self.expression})'


class SqrtNum(BaseNum):
    def __init__(self, string: str, k: str, expr: BaseExpr):
        super().__init__(string)
        self.k = to_num(k or '1')
        self.b = expr

    def eval(self, data):
        return to_num(
            float(self.b.eval(data) * (self.k ** 2)) ** 0.5
        )

    def __str__(self):
        k = "" if self.k == 1 else f"{self.k}"
        return f'{k}√{self.b}'


class FunctionNum(BaseNum):
    def __init__(self, string: str, expr: BaseExpr):
        super().__init__(string)
        self.expr = expr

    def eval(self, data):
        return lambda params: self.expr.eval(params)

    def __str__(self):
        return f'$( {self.expr} )'



class StrNum(BaseNum):
    def __init__(self, string: str):
        super().__init__(string)

    def eval(self, data):
        return self.string.strip('"')