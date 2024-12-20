"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import deprecated
from pyomo.core.pyomoobject import PyomoObject

logger = ...
native_logical_values = ...
def as_boolean(obj): # -> BooleanConstant:
    """
    A function that creates a BooleanConstant object that
    wraps Python Boolean values.

    Args:
        obj: The logical value that may be wrapped.

    Raises: TypeError if the object is in native_types and not in
        native_logical_types

    Returns: A true or false BooleanConstant or the original object
    """
    ...

class BooleanValue(PyomoObject):
    """
    This is the base class for Boolean values used in Pyomo.
    """
    __slots__ = ...
    __hash__ = ...
    def getname(self, fully_qualified=..., name_buffer=...): # -> str:
        """
        If this is a component, return the component's name on the owning
        block; otherwise return the value converted to a string
        """
        ...
    
    @property
    def name(self): # -> str:
        ...
    
    @property
    def local_name(self): # -> str:
        ...
    
    def is_constant(self): # -> Literal[False]:
        """Return True if this Logical value is a constant value"""
        ...
    
    def is_fixed(self): # -> Literal[False]:
        """Return True if this is a non-constant value that has been fixed"""
        ...
    
    @deprecated("is_relational() is deprecated in favor of " "is_expression_type(ExpressionType.RELATIONAL)", version='6.4.3')
    def is_relational(self): # -> Literal[False]:
        """
        Return True if this Logical value represents a relational expression.
        """
        ...
    
    def is_indexed(self): # -> Literal[False]:
        """Return True if this Logical value is an indexed object"""
        ...
    
    def is_numeric_type(self): # -> Literal[False]:
        """Boolean values are not numeric."""
        ...
    
    def is_logical_type(self): # -> Literal[True]:
        ...
    
    def __invert__(self):
        """
        Construct a NotExpression using operator '~'
        """
        ...
    
    def equivalent_to(self, other):
        """
        Construct an EquivalenceExpression between this BooleanValue and its operand.
        """
        ...
    
    def land(self, other):
        """
        Construct an AndExpression (Logical And) between this BooleanValue and `other`.
        """
        ...
    
    def __and__(self, other):
        """
        Construct an AndExpression using the '&' operator
        """
        ...
    
    def __rand__(self, other):
        """
        Construct an AndExpression using the '&' operator
        """
        ...
    
    def __iand__(self, other):
        """
        Construct an AndExpression using the '&' operator
        """
        ...
    
    def lor(self, other):
        """
        Construct an OrExpression (Logical OR) between this BooleanValue and `other`.
        """
        ...
    
    def __or__(self, other):
        """
        Construct an OrExpression using the '|' operator
        """
        ...
    
    def __ror__(self, other):
        """
        Construct an OrExpression using the '|' operator
        """
        ...
    
    def __ior__(self, other):
        """
        Construct an OrExpression using the '|' operator
        """
        ...
    
    def xor(self, other):
        """
        Construct an XorExpression using method "xor"
        """
        ...
    
    def __xor__(self, other):
        """
        Construct an XorExpression using the '^' operator
        """
        ...
    
    def __rxor__(self, other):
        """
        Construct an XorExpression using the '^' operator
        """
        ...
    
    def __ixor__(self, other):
        """
        Construct an XorExpression using the '^' operator
        """
        ...
    
    def implies(self, other):
        """
        Construct an ImplicationExpression using method "implies"
        """
        ...
    
    def to_string(self, verbose=..., labeler=..., smap=..., compute_values=...): # -> str:
        """
        Return a string representation of the expression tree.

        Args:
            verbose (bool): If :const:`True`, then the the string
                representation consists of nested functions.  Otherwise,
                the string representation is an algebraic equation.
                Defaults to :const:`False`.
            labeler: An object that generates string labels for
                variables in the expression tree.  Defaults to :const:`None`.

        Returns:
            A string representation for the expression tree.
        """
        ...
    


class BooleanConstant(BooleanValue):
    """An object that contains a constant Logical value.

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
    
    def is_potentially_variable(self): # -> Literal[False]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __nonzero__(self):
        ...
    
    def __bool__(self):
        ...
    
    def __call__(self, exception=...):
        """Return the constant value"""
        ...
    
    def pprint(self, ostream=..., verbose=...): # -> None:
        ...
    


