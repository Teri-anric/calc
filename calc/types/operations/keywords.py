from calc.types.base import BaseOperation
from . import registry_operation


@registry_operation()
class WhileKeyWordOperation(BaseOperation):
    OPERATOR = "#while"

    def eval(self, data):
        self.a.eval(data)
        r = 1
        while r is not None:
            r = self.b.eval(data)
        return 0


    def __str__(self):
        return f"({self.a} if {self.b})"


@registry_operation()
class IfKeyWordOperation(BaseOperation):
    OPERATOR = "#if"

    def eval(self, data):
        self.a.eval(data)
        return self.b.eval(data) or 0


    def __str__(self):
        return f"({self.a} if {self.b})"


@registry_operation()
class ToKeyWordOperation(BaseOperation):
    OPERATOR = "#to"

    def eval(self, data):
        if not self.a.eval(data):
            if isinstance(self.b, ElseKeyWordOperation):
                return self.b.b.eval(data)
            else:
                return None
        return self.b.eval(data)

    def __str__(self):
        return f"({self.a} to {self.b})"


@registry_operation()
class ElseKeyWordOperation(BaseOperation):
    OPERATOR = "#else"

    def eval(self, data):
        return self.a.eval(data)

    def __str__(self):
        return f"({self.a} else {self.b})"

