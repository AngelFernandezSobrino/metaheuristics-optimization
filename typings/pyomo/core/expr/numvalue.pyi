"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import deprecated
from pyomo.core.expr.numeric_expr import NumericValue
from pyomo.core.pyomoobject import PyomoObject

logger = ...
class NonNumericValue(PyomoObject):
    """An object that contains a non-numeric value

    Constructor Arguments:
        value           The initial value.
    """
    __slots__ = ...
    def __init__(self, value) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __call__(self, exception=...): # -> Any:
        ...
    


def is_constant(obj): # -> Literal[True]:
    """
    A utility function that returns a boolean that indicates
    whether the object is a constant.
    """
    ...

def is_fixed(obj): # -> Literal[True]:
    """
    A utility function that returns a boolean that indicates
    whether the input object's value is fixed.
    """
    ...

def is_variable_type(obj): # -> Literal[False]:
    """
    A utility function that returns a boolean indicating
    whether the input object is a variable.
    """
    ...

def is_potentially_variable(obj): # -> Literal[False]:
    """
    A utility function that returns a boolean indicating
    whether the input object can reference variables.
    """
    ...

def is_numeric_data(obj): # -> bool:
    """
    A utility function that returns a boolean indicating
    whether the input object is numeric and not potentially
    variable.
    """
    ...

def polynomial_degree(obj): # -> Literal[0]:
    """
    A utility function that returns an integer
    that indicates the polynomial degree for an
    object. boolean indicating
    """
    ...

_KnownConstants = ...
def as_numeric(obj): # -> NumericConstant:
    """
    A function that creates a NumericConstant object that
    wraps Python numeric values.

    This function also manages a cache of constants.

    NOTE:  This function is only intended for use when
        data is added to a component.

    Args:
        obj: The numeric value that may be wrapped.

    Raises: TypeError if the object is in native_types and not in
        native_numeric_types

    Returns: A NumericConstant object or the original object.
    """
    ...

@deprecated("check_if_numeric_type_and_cache() has been deprecated in " "favor of just calling as_numeric()", version='6.4.3')
def check_if_numeric_type_and_cache(obj): # -> NumericConstant:
    """Test if the argument is a numeric type by checking if we can add
    zero to it.  If that works, then we cache the value and return a
    NumericConstant object.

    """
    ...

class NumericConstant(NumericValue):
    """An object that contains a constant numeric value.

    Constructor Arguments:
        value           The initial value.
    """
    __slots__ = ...
    def __init__(self, value) -> None:
        ...
    
    def is_constant(self): # -> Literal[True]:
        ...
    
    def is_fixed(self): # -> Literal[True]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, exception=...): # -> Any:
        """Return the constant value"""
        ...
    
    def pprint(self, ostream=..., verbose=...): # -> None:
        ...
    


ZeroConstant = ...
