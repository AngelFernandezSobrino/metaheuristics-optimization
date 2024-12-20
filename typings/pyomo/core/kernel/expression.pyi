"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import deprecated
from pyomo.core.kernel.base import ICategorizedObject
from pyomo.core.expr.numvalue import NumericValue

class IIdentityExpression(NumericValue):
    """The interface for classes that simply wrap another
    expression and perform no additional operations.

    Derived classes should declare an _expr attribute or
    override all implemented methods.
    """
    __slots__ = ...
    PRECEDENCE = ...
    ASSOCIATIVITY = ...
    @property
    def expr(self):
        ...
    
    def __call__(self, exception=...): # -> None:
        """Compute the value of this expression.

        Args:
            exception (bool): Indicates if an exception
                should be raised when instances of
                NumericValue fail to evaluate due to one or
                more objects not being initialized to a
                numeric value (e.g, one or more variables in
                an algebraic expression having the value
                None). Default is :const:`True`.

        Returns:
            numeric value or None
        """
        ...
    
    def is_fixed(self): # -> Literal[True]:
        """A boolean indicating whether this expression is fixed."""
        ...
    
    def is_parameter_type(self): # -> Literal[False]:
        """A boolean indicating whether this expression is a parameter object."""
        ...
    
    def is_variable_type(self): # -> Literal[False]:
        """A boolean indicating whether this expression is a
        variable object."""
        ...
    
    def is_named_expression_type(self): # -> Literal[True]:
        """A boolean indicating whether this in a named expression."""
        ...
    
    def is_expression_type(self, expression_system=...): # -> Literal[True]:
        """A boolean indicating whether this in an expression."""
        ...
    
    @property
    def args(self): # -> tuple[Any]:
        """A tuple of subexpressions involved in this expressions operation."""
        ...
    
    def nargs(self): # -> Literal[1]:
        """Length of self._nargs()"""
        ...
    
    def arg(self, i):
        ...
    
    def polynomial_degree(self): # -> Literal[0]:
        """The polynomial degree of the stored expression."""
        ...
    
    def to_string(self, verbose=..., labeler=..., smap=..., compute_values=...):
        """Convert this expression into a string."""
        ...
    
    def create_node_with_local_data(self, values): # -> Self:
        """
        Construct an expression after constructing the
        contained expression.

        This class provides a consistent interface for constructing a
        node, which is used in tree visitor scripts.
        """
        ...
    
    def is_constant(self):
        ...
    
    def is_potentially_variable(self):
        ...
    
    def clone(self):
        ...
    


@deprecated("noclone() is deprecated and can be omitted: " "Pyomo expressions natively support shared subexpressions.", version='6.6.2')
def noclone(expr): # -> expression | data_expression:
    ...

class IExpression(ICategorizedObject, IIdentityExpression):
    """
    The interface for mutable expressions.
    """
    __slots__ = ...
    expr = ...
    def is_constant(self): # -> Literal[False]:
        """A boolean indicating whether this expression is constant."""
        ...
    
    def is_potentially_variable(self): # -> Literal[True]:
        """A boolean indicating whether this expression can
        reference variables."""
        ...
    
    def clone(self): # -> Self:
        """Return a clone of this expression (no-op)."""
        ...
    


class expression(IExpression):
    """A named, mutable expression."""
    _ctype = IExpression
    __slots__ = ...
    def __init__(self, expr=...) -> None:
        ...
    
    @property
    def expr(self): # -> None:
        ...
    
    @expr.setter
    def expr(self, expr): # -> None:
        ...
    


class data_expression(expression):
    """A named, mutable expression that is restricted to
    storage of data expressions. An exception will be raised
    if an expression is assigned that references (or is
    allowed to reference) variables."""
    __slots__ = ...
    def is_potentially_variable(self): # -> Literal[False]:
        """A boolean indicating whether this expression can
        reference variables."""
        ...
    
    def polynomial_degree(self): # -> Literal[0]:
        """Always return zero because we always validate
        that the stored expression can never reference
        variables."""
        ...
    
    @property
    def expr(self):
        ...
    
    @expr.setter
    def expr(self, expr): # -> None:
        ...
    


