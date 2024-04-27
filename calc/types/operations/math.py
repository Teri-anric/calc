from calc.types.base import BaseOperation
from . import registry_operation


@registry_operation()
class AddOperation(BaseOperation):
    OPERATOR = "+"

    def eval(self, data):
        return (
                self.a.eval(data)
                + self.b.eval(data)
        )


@registry_operation()
class SubOperation(BaseOperation):
    OPERATOR = "-"

    def eval(self, data):
        return (
                self.a.eval(data)
                - self.b.eval(data)
        )


@registry_operation()
class MulOperation(BaseOperation):
    OPERATOR = "*"

    def eval(self, data):
        return (
                self.a.eval(data)
                * self.b.eval(data)
        )


@registry_operation()
class DivOperation(BaseOperation):
    OPERATOR = "/"

    def eval(self, data):
        return (
                self.a.eval(data)
                / self.b.eval(data)
        )


@registry_operation("**")
@registry_operation()
class PowOperation(BaseOperation):
    OPERATOR = "^"

    def eval(self, data):
        return (
                self.a.eval(data)
                ** self.b.eval(data)
        )
