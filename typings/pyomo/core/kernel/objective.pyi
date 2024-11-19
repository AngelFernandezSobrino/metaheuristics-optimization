"""
This type stub file was generated by pyright.
"""

from pyomo.core.kernel.expression import IExpression

class IObjective(IExpression):
    """
    The interface for optimization objectives.
    """
    __slots__ = ...
    sense = ...
    def is_minimizing(self): # -> Any:
        ...
    


class objective(IObjective):
    """An optimization objective."""
    _ctype = IObjective
    __slots__ = ...
    def __init__(self, expr=..., sense=...) -> None:
        ...
    
    @property
    def expr(self): # -> NumericConstant | None:
        ...
    
    @expr.setter
    def expr(self, expr): # -> None:
        ...
    
    @property
    def sense(self): # -> ObjectiveSense | None:
        ...
    
    @sense.setter
    def sense(self, sense): # -> None:
        """Set the sense (direction) of this objective."""
        ...
    


