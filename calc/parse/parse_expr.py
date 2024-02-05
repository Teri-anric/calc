
def parse_expression(expression: str) -> "BaseExpr":
    # print(expression)
    lst = screech_operation(expression)
    if len(lst) == 1:
        num = lst[0].strip()
        # expression "(2+7)"
        if "(" == num[0] and num[-1] == ')':
            return parse_expression(
                num[1:-1]  # cut ()
            )
        # return num
        return parse_num(num)
    else:
        # build math tree
        return build_tree(lst)


from . import screech_operation
from . import parse_num
from . import build_tree