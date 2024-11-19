"""
This type stub file was generated by pyright.
"""

from pyomo.core.expr.numvalue import NumericValue
from pyomo.core.kernel.base import ICategorizedObject

class IParameter(ICategorizedObject, NumericValue):
    """The interface for mutable numeric data."""
    __slots__ = ...
    def __call__(self, exception=...):
        """Computes the numeric value of this object."""
        ...
    
    def is_constant(self): # -> Literal[False]:
        """A boolean indicating that this parameter is constant."""
        ...
    
    def is_parameter_type(self): # -> Literal[False]:
        """A boolean indicating that this is a parameter object."""
        ...
    
    def is_variable_type(self): # -> Literal[False]:
        """A boolean indicating that this is a variable object."""
        ...
    
    def is_fixed(self): # -> Literal[True]:
        """A boolean indicating that this parameter is fixed."""
        ...
    
    def is_potentially_variable(self): # -> Literal[False]:
        """Returns :const:`False` because this object can
        never reference variables."""
        ...
    
    def polynomial_degree(self): # -> Literal[0]:
        """Always return zero because we always validate
        that the stored expression can never reference
        variables."""
        ...
    


class parameter(IParameter):
    """A object for storing a mutable, numeric value that
    can be used to build a symbolic expression."""
    _ctype = IParameter
    __slots__ = ...
    def __init__(self, value=...) -> None:
        ...
    
    def __call__(self, exception=...): # -> None:
        """Computes the numeric value of this object."""
        ...
    
    @property
    def value(self): # -> None:
        """The value of the parameter"""
        ...
    
    @value.setter
    def value(self, value): # -> None:
        ...
    


class functional_value(IParameter):
    """An object for storing a numeric function that can be
    used in a symbolic expression.

    Note that models making use of this object may require
    the dill module for serialization.
    """
    _ctype = IParameter
    __slots__ = ...
    def __init__(self, fn=...) -> None:
        ...
    
    def __call__(self, exception=...): # -> None:
        ...
    
    @property
    def fn(self): # -> None:
        """The function stored with this object"""
        ...
    
    @fn.setter
    def fn(self, fn): # -> None:
        ...
    

