from .. import types

is_word = lambda s: s.islower() or s.isupper()
is_numeric = lambda s: s.isdigit() or s == '.'

def parse_num(num):
    if "π" == num:
        return types.PiNum(num)

    name, _, q = num.partition('(')
    if all(map(is_word, name)) and _ == '(':
        return types.FuncNum(num)

    if all(map(is_word, num)):
        return types.ConstNum(num)

    if "√" in num:
        return types.SqrtNum(num)

    return types.Num(num)
