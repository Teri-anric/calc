import math
from fractions import Fraction
from inspect import getfullargspec

from .base import BaseExpr, BaseNum


__all__ = ['default_to_num', 'Num', 'ConstNum', 'PiNum', 'FuncNum', 'SqrtNum', 'FunctionNum', 'StrNum']

default_to_num = Fraction

def to_num(s_num, data=None):
    if data:
        func = data.get('__to_num', default_to_num)
        return func(s_num)
    return default_to_num(s_num)


class Num(BaseNum):
    def eval(self, data):
        return to_num(self.string, data)


class ConstNum(BaseNum):
    def eval(self, data):
        return to_num(data[self.string], data)


class PiNum(BaseNum):
    def eval(self, data):
        return to_num(math.pi, data)


class FuncNum(BaseNum):
    def __init__(self, string: str, name: str, expr: BaseExpr):
        super().__init__(string)
        self.name = name.strip()
        self.expression = expr

    def eval(self, data: dict):
        func = data[self.name]
        spec = getfullargspec(func)
        if '_gdata' not in spec.args:
            arg = self.expression.eval(data)
            result = func(arg)
        else:
            local_data = data.copy()
            _ = self.expression.eval(local_data)
            result = func(local_data, _gdata=data)
        return to_num(result, data)

    def __str__(self):
        return f'{self.name}({self.expression})'


class SqrtNum(BaseNum):
    def __init__(self, string: str, k: str, expr: BaseExpr):
        super().__init__(string)
        self.k = k or '1'
        self.b = expr

    def eval(self, data):
        full_part = to_num(self.k, data) ** 2
        reqult = self.b.eval(data) * full_part
        return to_num(reqult ** 0.5, data)

    def __str__(self):
        k = "" if self.k == 1 else f"{self.k}"
        return f'{k}√{self.b}'


class FunctionNum(BaseNum):
    def __init__(self, string: str, expr: BaseExpr):
        super().__init__(string)
        self.expr = expr

    def eval(self, data):
        return lambda params, _gdata: self.expr.eval(params)

    def __str__(self):
        return f'$( {self.expr} )'



class StrNum(BaseNum):
    def __init__(self, string: str):
        super().__init__(string)

    def eval(self, data):
        return self.string.strip('"')