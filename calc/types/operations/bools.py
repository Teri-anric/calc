from calc.types.base import BaseOperation
from . import registry_operation


@registry_operation()
class GeOperation(BaseOperation):
    OPERATOR = ">="

    def eval(self, data):
        return (
                self.a.eval(data)
                >= self.b.eval(data)
        )

@registry_operation()
class LeOperation(BaseOperation):
    OPERATOR = "<="

    def eval(self, data):
        return (
                self.a.eval(data)
                <= self.b.eval(data)
        )

@registry_operation()
class GtOperation(BaseOperation):
    OPERATOR = ">"

    def eval(self, data):
        return (
                self.a.eval(data)
                > self.b.eval(data)
        )

@registry_operation()
class LtOperation(BaseOperation):
    OPERATOR = "<"

    def eval(self, data):
        return (
                self.a.eval(data)
                < self.b.eval(data)
        )

@registry_operation()
class NeOperation(BaseOperation):
    OPERATOR = "!="

    def eval(self, data):
        return (
                self.a.eval(data)
                != self.b.eval(data)
        )

@registry_operation()
class EqOperation(BaseOperation):
    OPERATOR = "=="

    def eval(self, data):
        return (
                self.a.eval(data)
                == self.b.eval(data)
        )
