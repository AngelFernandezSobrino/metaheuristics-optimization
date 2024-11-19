"""
This type stub file was generated by pyright.
"""

import pyomo.core.expr as EXPR

_operatorMap = ...
_pyomo_operator_map = ...
_functionMap = ...
class PyomoSympyBimap:
    def __init__(self) -> None:
        ...
    
    def getPyomoSymbol(self, sympy_object, default=...):
        ...
    
    def getSympySymbol(self, pyomo_object): # -> Any:
        ...
    
    def sympyVars(self): # -> dict_keys[Any, Any]:
        ...
    


class Pyomo2SympyVisitor(EXPR.StreamBasedExpressionVisitor):
    def __init__(self, object_map, keep_mutable_parameters=...) -> None:
        ...
    
    def initializeWalker(self, expr): # -> tuple[Literal[False], Any] | tuple[Literal[True], None] | tuple[Literal[False], Any | None]:
        ...
    
    def exitNode(self, node, values):
        ...
    
    def beforeChild(self, node, child, child_idx): # -> tuple[Literal[False], Any] | tuple[Literal[True], None] | tuple[Literal[False], Any | None]:
        ...
    


class Sympy2PyomoVisitor(EXPR.StreamBasedExpressionVisitor):
    def __init__(self, object_map) -> None:
        ...
    
    def initializeWalker(self, expr): # -> tuple[Literal[False], float | Any] | tuple[Literal[True], None]:
        ...
    
    def enterNode(self, node): # -> tuple[Any, list[Any]]:
        ...
    
    def exitNode(self, node, values):
        """Visit nodes that have been expanded"""
        ...
    
    def beforeChild(self, node, child, child_idx): # -> tuple[Literal[False], float | Any] | tuple[Literal[True], None]:
        ...
    


def sympyify_expression(expr, keep_mutable_parameters=...): # -> tuple[PyomoSympyBimap, Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | None]:
    """Convert a Pyomo expression to a Sympy expression"""
    ...

def sympy2pyomo_expression(expr, object_map): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
    ...

