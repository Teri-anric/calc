from typing import List

from .. import types


def build_tree(lst: List[str]) -> 'types.Base':
    for op in types.OPERATIONS:
        i = 0
        n = len(lst)
        while i < n:
            if lst[i] == op:
                Oprtation = types.OPERATIONS_CLASS.get(op)
                lst[i] = Oprtation(
                    lst[i - 1],  # Left num
                    lst[i + 1]  # Right num
                )

                del lst[i - 1]  # del Left num
                del lst[i]  # del Right num

                i -= 1
                n = len(lst)  # update len list
            else:
                i += 1
    return lst[0]
