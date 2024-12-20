"""
This type stub file was generated by pyright.
"""

from pyomo.core.expr.visitor import StreamBasedExpressionVisitor
from pyomo.repn.util import BeforeChildDispatcher, ExitNodeDispatcher

inf = ...
logger = ...
class ExpressionBoundsBeforeChildDispatcher(BeforeChildDispatcher):
    __slots__ = ...
    def __init__(self) -> None:
        ...
    


_unary_function_dispatcher = ...
class ExpressionBoundsExitNodeDispatcher(ExitNodeDispatcher):
    def unexpected_expression_type(self, visitor, node, *args): # -> tuple[float, float] | tuple[_bool_flag, _bool_flag]:
        ...
    


class ExpressionBoundsVisitor(StreamBasedExpressionVisitor):
    """
    Walker to calculate bounds on an expression, from leaf to root, with
    caching of terminal node bounds (Vars and Expressions)

    NOTE: If anything changes on the model (e.g., Var bounds, fixing, mutable
    Param values, etc), then you need to either create a new instance of this
    walker, or clear self.leaf_bounds!

    Parameters
    ----------
    leaf_bounds: ComponentMap in which to cache bounds at leaves of the expression
        tree
    feasibility_tol: float, feasibility tolerance for interval arithmetic
        calculations
    use_fixed_var_values_as_bounds: bool, whether or not to use the values of
        fixed Vars as the upper and lower bounds for those Vars or to instead
        ignore fixed status and use the bounds. Set to 'True' if you do not
        anticipate the fixed status of Variables to change for the duration that
        the computed bounds should be valid.
    """
    _before_child_handlers = ...
    _operator_dispatcher = ...
    def __init__(self, leaf_bounds=..., feasibility_tol=..., use_fixed_var_values_as_bounds=...) -> None:
        ...
    
    def initializeWalker(self, expr): # -> tuple[Literal[False], Any] | tuple[Literal[True], Any]:
        ...
    
    def beforeChild(self, node, child, child_idx):
        ...
    
    def exitNode(self, node, data):
        ...
    


