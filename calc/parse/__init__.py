from ..types.base import BaseExpr

from calc.parse.build_tree import build_tree
from calc.parse.parse_num import parse_num
from calc.parse.sreach_operation import screech_operation

def parse_expression(expression: str) -> BaseExpr:
    return _parse_expression(expression)


from calc.parse.parse_expr import parse_expression as _parse_expression