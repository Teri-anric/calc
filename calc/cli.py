import math
import sys
from pathlib import Path

from calc import parse_expression
from calc.types.num import to_num

HELP_MESSAGE = """"""


def console(data: dict, _gdata: dict):
    end = "\n" if data.get("end", True) else ""
    if "out" in data:
        print(data["out"], end=end)
    if "ch" in data:
        print(chr(int(data["ch"])), end=end)
    if "in" in data:
        return to_num(input(), _gdata)
    return to_num(0, _gdata)


def interactive_mode(data):
    while True:
        tree = parse_expression(input(">>> "))
        print(tree.eval(data))


def main():
    args = sys.argv
    # generate data
    data = {}
    data.update(math.__dict__)
    data.update(console=console)
    # generate math tree
    if not Path(args[-1]).exists():
        return interactive_mode(data)

    with open(args[-1], "r", encoding="utf-8") as fp:
        tree = parse_expression(fp.read())
        # eval tree
    if "-tree" in args:
        print(tree)
    return tree.eval(data)
