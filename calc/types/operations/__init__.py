from typing import List, Dict, Type

from calc.types.base import BaseOperation

__all__ = ["ALL_OPERATIONS", "MAP_OPERATIONS"]

ALL_OPERATIONS: List[str] = []
MAP_OPERATIONS: Dict[str, Type[BaseOperation]] = {}


def registry_operation(operator: str = None):
    def decorator(cls: Type[BaseOperation]):
        ALL_OPERATIONS.insert(0, operator or cls.OPERATOR)
        MAP_OPERATIONS[operator or cls.OPERATOR] = cls
        return cls

    return decorator


from .math import *
from .keywords import *
from .syntax import *
from .bools import *
