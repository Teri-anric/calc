from calc.types import ConstNum
from calc.types.base import BaseOperation
from . import registry_operation


@registry_operation("\n")
@registry_operation()
class IdentOperation(BaseOperation):
    OPERATOR = ";"

    def eval(self, data):
        self.a.eval(data)
        return self.b.eval(data)

    def __str__(self):
        return f"({self.a}; {self.b})"


@registry_operation()
class AssignOperation(BaseOperation):
    OPERATOR = "="
    a: ConstNum

    def __init__(self, a, b):
        super().__init__(a, b)
        if not isinstance(self.a, ConstNum):
            raise TypeError(f"Operation '=', left operand must be ConstNum")

    def eval(self, data):
        result = self.b.eval(data)
        data[self.a.string] = result
        return result

    def __str__(self):
        return f"({self.a} = {self.b})"
