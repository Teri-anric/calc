from typing import List

from calc.types import ALL_OPERATIONS

class BracketsManager:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end
        self.count = 0

    def test(self, i: int, full: str):
        if full[i:i+len(self.start)] == self.start:
            self.count += 1
        elif full[i:i+len(self.end)] == self.end:
            self.count -= 1
        return self.count

    def __bool__(self):
        return bool(self.count)

class IdentsManager:
    def __init__(self, ident: str):
        self.ident = ident
        self.available = False

    def test(self, i: int, full: str):
        if full[i:i+len(self.ident)] == self.ident:
            self.available = not self.available
        return self.available

    def __bool__(self):
        return bool(self.available)

def screech_operation(expression: str) -> List[str]:
    if not expression:
        return []
    lst = []
    num = ""
    brackets = BracketsManager("(", ")")
    str_idents = IdentsManager('"')
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch in (' ', '', '\n'):
            i += 1
            if brackets or str_idents:
                num += ch
            continue
        if not brackets.test(i, expression) and not str_idents.test(i, expression):
            for op in ALL_OPERATIONS:
                if op == expression[i:i+len(op)]:
                    lst += [num]  # add left num
                    lst += [op]  # add oprtation
                    num = ""  # clear num
                    ch = ""  # clear current char
                    i += len(op) - 1
                    break
        num += ch  # add chr to numeric
        i += 1
    lst += [num]  # add last element
    return lst
