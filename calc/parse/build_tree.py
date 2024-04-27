from typing import List

from calc.types import BaseExpr, StrNum, MAP_OPERATIONS, ALL_OPERATIONS, PiNum, FuncNum, ConstNum, SqrtNum, FunctionNum, Num
from ..types.base import BaseNum, VoidExpr
from .sreach_operation import screech_operation


def build_tree(lst: List[str]) -> BaseExpr:
    for op in ALL_OPERATIONS:
        i = 0
        n = len(lst)
        while i < n:
            if lst[i] == op:
                Oprtation = MAP_OPERATIONS.get(op)
                # left
                left_operand = lst[i - 1]
                if isinstance(left_operand, str):
                    left_operand = parse_expression(left_operand)
                # right
                right_operand = lst[i + 1]
                if isinstance(right_operand, str):
                    right_operand = parse_expression(right_operand)
                # create operator
                lst[i] = Oprtation(
                    left_operand,  # Left num
                    right_operand  # Right num
                )

                del lst[i - 1]  # del Left num
                del lst[i]  # del Right num

                i -= 1
                n = len(lst)  # update len list
            else:
                i += 1
    return lst[0]


def parse_expression(expression: str) -> BaseExpr:
    # print(expression)
    lst = screech_operation(expression)
    if len(lst) == 0:
        return VoidExpr()
    if len(lst) == 1:
        num = lst[0].strip()
        # expression "(2+7)"
        # print(expression, num)
        if num.startswith("(") and num.endswith(")"):
            return parse_expression(
                num[1:-1]  # cut ()
            )
        # return num
        return parse_num(num)
    else:
        # build math tree
        return build_tree(lst)


is_word = lambda s: s.islower() or s.isupper()
is_numeric = lambda s: s.isdigit() or s == '.'


def parse_num(num) -> BaseNum:
    if num.startswith('"') and num.endswith('"'):
        return StrNum(num)
    if "π" == num:
        return PiNum(num)

    if num.startswith("$"):
        return FunctionNum(num, parse_expression(num[1:]))

    name, _, q = num.partition('(')
    if all(map(is_word, name)) and _ == '(':
        return FuncNum(num, name, parse_expression("(" + q))

    if all(map(is_word, num)):
        return ConstNum(num)

    if "√" in num:
        a, _, b = num.partition('√')
        return SqrtNum(num, a, parse_expression(b))

    return Num(num)
