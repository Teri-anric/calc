import math
from fractions import Fraction

from calc import parse_expression


def eval_expression(expression, **kwargs):
    # generate data
    data = {}
    data.update(math.__dict__)
    data.update(kwargs)
    # generate math tree
    tree = parse_expression(expression)
    print("Tree: ", tree)
    # eval tree
    result = tree.eval(data)

    # round big numeric
    if len(str(result)) > 20:
        result = Fraction(
            round(result, 10)
        )
    return result


if __name__ == '__main__':
    result = eval_expression(input("Please enter an expression: "))
    print("Result:", result)