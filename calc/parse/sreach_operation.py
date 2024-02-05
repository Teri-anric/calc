from typing import List

from calc import types


def screech_operation(expression: str) -> List[str]:
    lst = []
    num = ""
    count = 0  # count ()
    for ch in expression:
        if '(' == ch:
            count += 1
        elif ')' == ch:
            count -= 1

        if not count and ch in types.OPERATIONS:
            lst += [num]  # add left num
            lst += [ch]  # add oprtation
            num = ""  # clear num
            continue;

        num += ch  # add chr to numeric

    lst += [num]  # add last element
    return lst
