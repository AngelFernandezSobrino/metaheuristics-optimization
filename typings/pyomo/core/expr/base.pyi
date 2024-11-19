"""
This type stub file was generated by pyright.
"""

from pyomo.core.pyomoobject import PyomoObject

class ExpressionBase(PyomoObject):
    """The base class for all Pyomo expression systems.

    This class is used to define nodes in a general expression tree.
    Individual expression systems (numeric, logical, etc.) will mix this
    class in with their fundamental base data type (NumericValue,
    BooleanValue, etc) to form the base node of that expression system.
    """
    __slots__ = ...
    PRECEDENCE = ...
    ASSOCIATIVITY = ...
    def nargs(self):
        """Returns the number of child nodes.

        Note
        ----

        Individual expression nodes may use different internal storage
        schemes, so it is imperative that developers use this method and
        not assume the existence of a particular attribute!

        Returns
        -------
        int: A nonnegative integer that is the number of child nodes.

        """
        ...
    
    def arg(self, i):
        """Return the i-th child node.

        Parameters
        ----------
        i: int
            Index of the child argument to return

        Returns: The i-th child node.

        """
        ...
    
    @property
    def args(self):
        """Return the child nodes

        Returns
        -------
        list or tuple:
            Sequence containing only the child nodes of this node.  The
            return type depends on the node storage model.  Users are
            not permitted to change the returned data (even for the case
            of data returned as a list), as that breaks the promise of
            tree immutability.

        """
        ...
    
    def __call__(self, exception=...): # -> Any:
        """Evaluate the value of the expression tree.

        Parameters
        ----------
        exception: bool
            If :const:`False`, then an exception raised while evaluating
            is captured, and the value returned is :const:`None`.
            Default is :const:`True`.

        Returns
        -------
        The value of the expression or :const:`None`.

        """
        ...
    
    def __str__(self) -> str:
        """Returns a string description of the expression.

        Note:

        The value of ``pyomo.core.expr.expr_common.TO_STRING_VERBOSE``
        is used to configure the execution of this method.  If this
        value is :const:`True`, then the string representation is a
        nested function description of the expression.  The default is
        :const:`False`, which returns an algebraic (infix notation)
        description of the expression.

        Returns
        -------
        str
        """
        ...
    
    def to_string(self, verbose=..., labeler=..., smap=..., compute_values=...): # -> Any:
        """Return a string representation of the expression tree.

        Parameters
        ----------
        verbose: bool
            If :const:`True`, then the string representation
            consists of nested functions.  Otherwise, the string
            representation is an algebraic (infix notation) equation.
            Defaults to :const:`False`.

        labeler:
            An object that generates string labels for variables in the
            expression tree.  Defaults to :const:`None`.

        smap:
            If specified, this
            :class:`SymbolMap <pyomo.core.expr.symbol_map.SymbolMap>`
            is used to cache labels for variables.

        compute_values (bool):
            If :const:`True`, then parameters and fixed variables are
            evaluated before the expression string is generated.
            Default is :const:`False`.

        Returns:
            A string representation for the expression tree.

        """
        ...
    
    def getname(self, *args, **kwds):
        """Return the text name of a function associated with this expression
        object.

        In general, no arguments are passed to this function.

        Args:
            *arg: a variable length list of arguments
            **kwds: keyword arguments

        Returns:
            A string name for the function.

        """
        ...
    
    def clone(self, substitute=...): # -> Any:
        """
        Return a clone of the expression tree.

        Note:
            This method does not clone the leaves of the
            tree, which are numeric constants and variables.
            It only clones the interior nodes, and
            expression leaf nodes like
            :class:`_MutableLinearExpression<pyomo.core.expr.current._MutableLinearExpression>`.
            However, named expressions are treated like
            leaves, and they are not cloned.

        Args:
            substitute (dict): a dictionary that maps object ids to clone
                objects generated earlier during the cloning process.

        Returns:
            A new expression tree.
        """
        ...
    
    def create_node_with_local_data(self, args, classtype=...): # -> Self:
        """
        Construct a node using given arguments.

        This method provides a consistent interface for constructing a
        node, which is used in tree visitor scripts.  In the simplest
        case, this returns::

            self.__class__(args)

        But in general this creates an expression object using local
        data as well as arguments that represent the child nodes.

        Args:
            args (list): A list of child nodes for the new expression
                object

        Returns:
            A new expression object with the same type as the current
            class.
        """
        ...
    
    def is_constant(self): # -> Literal[False]:
        """Return True if this expression is an atomic constant

        This method contrasts with the is_fixed() method.  This method
        returns True if the expression is an atomic constant, that is it
        is composed exclusively of constants and immutable parameters.
        NumericValue objects returning is_constant() == True may be
        simplified to their numeric value at any point without warning.

        Note:  This defaults to False, but gets redefined in sub-classes.
        """
        ...
    
    def is_fixed(self): # -> Any:
        """
        Return :const:`True` if this expression contains no free variables.

        Returns:
            A boolean.
        """
        ...
    
    def is_potentially_variable(self): # -> Literal[True]:
        """
        Return :const:`True` if this expression might represent
        a variable expression.

        This method returns :const:`True` when (a) the expression
        tree contains one or more variables, or (b) the expression
        tree contains a named expression. In both cases, the
        expression cannot be treated as constant since (a) the variables
        may not be fixed, or (b) the named expressions may be changed
        at a later time to include non-fixed variables.

        Returns:
            A boolean.  Defaults to :const:`True` for expressions.
        """
        ...
    
    def is_named_expression_type(self): # -> Literal[False]:
        """
        Return :const:`True` if this object is a named expression.

        This method returns :const:`False` for this class, and it
        is included in other classes within Pyomo that are not named
        expressions, which allows for a check for named expressions
        without evaluating the class type.

        Returns:
            A boolean.
        """
        ...
    
    def is_expression_type(self, expression_system=...): # -> Literal[True]:
        """
        Return :const:`True` if this object is an expression.

        This method obviously returns :const:`True` for this class, but it
        is included in other classes within Pyomo that are not expressions,
        which allows for a check for expressions without
        evaluating the class type.

        Returns:
            A boolean.
        """
        ...
    
    def size(self): # -> Any:
        """
        Return the number of nodes in the expression tree.

        Returns:
            A nonnegative integer that is the number of interior and leaf
            nodes in the expression tree.
        """
        ...
    


class NPV_Mixin:
    __slots__ = ...
    def is_potentially_variable(self): # -> Literal[False]:
        ...
    
    def create_node_with_local_data(self, args, classtype=...):
        ...
    
    def potentially_variable_base_class(self): # -> type:
        ...
    


class ExpressionArgs_Mixin:
    __slots__ = ...
    def __init__(self, args) -> None:
        ...
    
    def nargs(self): # -> int:
        ...
    
    @property
    def args(self): # -> Any:
        """
        Return the child nodes

        Returns
        -------
        list or tuple:
            Sequence containing only the child nodes of this node.  The
            return type depends on the node storage model.  Users are
            not permitted to change the returned data (even for the case
            of data returned as a list), as that breaks the promise of
            tree immutability.
        """
        ...
    


