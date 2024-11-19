"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import deprecated

logger = ...
currentframe = ...
def get_stack_depth(): # -> int:
    ...

RECURSION_LIMIT = ...
class RevertToNonrecursive(Exception):
    ...


class StreamBasedExpressionVisitor:
    """This class implements a generic stream-based expression walker.

    This visitor walks an expression tree using a depth-first strategy
    and generates a full event stream similar to other tree visitors
    (e.g., the expat XML parser).  The following events are triggered
    through callback functions as the traversal enters and leaves nodes
    in the tree:

    ::

       initializeWalker(expr) -> walk, result
       enterNode(N1) -> args, data
       {for N2 in args:}
         beforeChild(N1, N2) -> descend, child_result
           enterNode(N2) -> N2_args, N2_data
           [...]
           exitNode(N2, n2_data) -> child_result
         acceptChildResult(N1, data, child_result) -> data
         afterChild(N1, N2) -> None
       exitNode(N1, data) -> N1_result
       finalizeWalker(result) -> result

    Individual event callbacks match the following signatures:

    walk, result = initializeWalker(self, expr):

         initializeWalker() is called to set the walker up and perform
         any preliminary processing on the root node.  The method returns
         a flag indicating if the tree should be walked and a result.  If
         `walk` is True, then result is ignored.  If `walk` is False,
         then `result` is returned as the final result from the walker,
         bypassing all other callbacks (including finalizeResult).

    args, data = enterNode(self, node):

         enterNode() is called when the walker first enters a node (from
         above), and is passed the node being entered.  It is expected to
         return a tuple of child `args` (as either a tuple or list) and a
         user-specified data structure for collecting results.  If None
         is returned for args, the node's args attribute is used for
         expression types and the empty tuple for leaf nodes.  Returning
         None is equivalent to returning (None,None).  If the callback is
         not defined, the default behavior is equivalent to returning
         (None, []).

    node_result = exitNode(self, node, data):

         exitNode() is called after the node is completely processed (as
         the walker returns up the tree to the parent node).  It is
         passed the node and the results data structure (defined by
         enterNode() and possibly further modified by
         acceptChildResult()), and is expected to return the "result" for
         this node.  If not specified, the default action is to return
         the data object from enterNode().

    descend, child_result = beforeChild(self, node, child, child_idx):

         beforeChild() is called by a node for every child before
         entering the child node.  The node, child node, and child index
         (position in the args list from enterNode()) are passed as
         arguments.  beforeChild should return a tuple (descend,
         child_result).  If descend is False, the child node will not be
         entered and the value returned to child_result will be passed to
         the node's acceptChildResult callback.  Returning None is
         equivalent to (True, None).  The default behavior if not
         specified is equivalent to (True, None).

    data = acceptChildResult(self, node, data, child_result, child_idx):

         acceptChildResult() is called for each child result being
         returned to a node.  This callback is responsible for recording
         the result for later processing or passing up the tree.  It is
         passed the node, result data structure (see enterNode()), child
         result, and the child index (position in args from enterNode()).
         The data structure (possibly modified or replaced) must be
         returned.  If acceptChildResult is not specified, it does
         nothing if data is None, otherwise it calls data.append(result).

    afterChild(self, node, child, child_idx):

         afterChild() is called by a node for every child node
         immediately after processing the node is complete before control
         moves to the next child or up to the parent node.  The node,
         child node, an child index (position in args from enterNode())
         are passed, and nothing is returned.  If afterChild is not
         specified, no action takes place.

    finalizeResult(self, result):

         finalizeResult() is called once after the entire expression tree
         has been walked.  It is passed the result returned by the root
         node exitNode() callback.  If finalizeResult is not specified,
         the walker returns the result obtained from the exitNode
         callback on the root node.

    Clients interact with this class by either deriving from it and
    implementing the necessary callbacks (see above), assigning callable
    functions to an instance of this class, or passing the callback
    functions as arguments to this class' constructor.

    """
    client_methods = ...
    def __init__(self, **kwds) -> None:
        ...
    
    def walk_expression(self, expr): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
        """Walk an expression, calling registered callbacks.

        This is the standard interface for running the visitor.  It
        defaults to using an efficient recursive implementation of the
        visitor, falling back on :py:meth:`walk_expression_nonrecursive`
        if the recursion stack gets too deep.

        """
        ...
    
    def walk_expression_nonrecursive(self, expr): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | None:
        """Nonrecursively walk an expression, calling registered callbacks.

        This routine is safer than the recursive walkers for deep (or
        unbalanced) trees.  It is, however, slightly slower than the
        recursive implementations.

        """
        ...
    


class SimpleExpressionVisitor:
    """
    Note:
        This class is a customization of the PyUtilib :class:`SimpleVisitor
        <pyutilib.misc.visitor.SimpleVisitor>` class that is tailored
        to efficiently walk Pyomo expression trees.  However, this class
        is not a subclass of the PyUtilib :class:`SimpleVisitor
        <pyutilib.misc.visitor.SimpleVisitor>` class because all key methods
        are reimplemented.
    """
    def visit(self, node): # -> None:
        """
        Visit a node in an expression tree and perform some operation on
        it.

        This method should be over-written by a user
        that is creating a sub-class.

        Args:
            node: a node in an expression tree

        Returns:
            nothing
        """
        ...
    
    def finalize(self): # -> None:
        """
        Return the "final value" of the search.

        The default implementation returns :const:`None`, because
        the traditional visitor pattern does not return a value.

        Returns:
            The final value after the search.  Default is :const:`None`.
        """
        ...
    
    def xbfs(self, node): # -> None:
        """
        Breadth-first search of an expression tree,
        except that leaf nodes are immediately visited.

        Note:
            This method has the same functionality as the
            PyUtilib :class:`SimpleVisitor.xbfs <pyutilib.misc.visitor.SimpleVisitor.xbfs>`
            method.  The difference is that this method
            is tailored to efficiently walk Pyomo expression trees.

        Args:
            node: The root node of the expression tree that is searched.

        Returns:
            The return value is determined by the :func:`finalize` function,
            which may be defined by the user.  Defaults to :const:`None`.
        """
        ...
    
    def xbfs_yield_leaves(self, node): # -> Generator[Never, Any, None]:
        """
        Breadth-first search of an expression tree, except that
        leaf nodes are immediately visited.

        Note:
            This method has the same functionality as the
            PyUtilib :class:`SimpleVisitor.xbfs_yield_leaves <pyutilib.misc.visitor.SimpleVisitor.xbfs_yield_leaves>`
            method.  The difference is that this method
            is tailored to efficiently walk Pyomo expression trees.

        Args:
            node: The root node of the expression tree
                that is searched.

        Returns:
            The return value is determined by the :func:`finalize` function,
            which may be defined by the user.  Defaults to :const:`None`.
        """
        ...
    


class ExpressionValueVisitor:
    """
    Note:
        This class is a customization of the PyUtilib :class:`ValueVisitor
        <pyutilib.misc.visitor.ValueVisitor>` class that is tailored
        to efficiently walk Pyomo expression trees.  However, this class
        is not a subclass of the PyUtilib :class:`ValueVisitor
        <pyutilib.misc.visitor.ValueVisitor>` class because all key methods
        are reimplemented.
    """
    def visit(self, node, values): # -> None:
        """
        Visit a node in a tree and compute its value using
        the values of its children.

        This method should be over-written by a user
        that is creating a sub-class.

        Args:
            node: a node in a tree
            values: a list of values of this node's children

        Returns:
            The *value* for this node, which is computed using :attr:`values`
        """
        ...
    
    def visiting_potential_leaf(self, node):
        """
        Visit a node and return its value if it is a leaf.

        Note:
            This method needs to be over-written for a specific
            visitor application.

        Args:
            node: a node in a tree

        Returns:
            A tuple: ``(flag, value)``.   If ``flag`` is False,
            then the node is not a leaf and ``value`` is :const:`None`.
            Otherwise, ``value`` is the computed value for this node.
        """
        ...
    
    def finalize(self, ans):
        """
        This method defines the return value for the search methods
        in this class.

        The default implementation returns the value of the
        initial node (aka the root node), because
        this visitor pattern computes and returns value for each
        node to enable the computation of this value.

        Args:
            ans: The final value computed by the search method.

        Returns:
            The final value after the search. Defaults to simply
            returning :attr:`ans`.
        """
        ...
    
    def dfs_postorder_stack(self, node):
        """
        Perform a depth-first search in postorder using a stack
        implementation.

        Note:
            This method has the same functionality as the
            PyUtilib :class:`ValueVisitor.dfs_postorder_stack <pyutilib.misc.visitor.ValueVisitor.dfs_postorder_stack>`
            method.  The difference is that this method
            is tailored to efficiently walk Pyomo expression trees.

        Args:
            node: The root node of the expression tree
                that is searched.

        Returns:
            The return value is determined by the :func:`finalize` function,
            which may be defined by the user.
        """
        ...
    


def replace_expressions(expr, substitution_map, descend_into_named_expressions=..., remove_named_expressions=...): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
    """

    Parameters
    ----------
    expr : Pyomo expression
       The source expression
    substitution_map : dict
       A dictionary mapping object ids in the source to the replacement objects.
    descend_into_named_expressions : bool
       True if replacement should go into named expression objects, False to halt at
       a named expression
    remove_named_expressions : bool
       True if the named expressions should be replaced with a standard expression,
       and False if the named expression should be left in place

    Returns
    -------
       Pyomo expression : returns the new expression object
    """
    ...

class ExpressionReplacementVisitor(StreamBasedExpressionVisitor):
    def __init__(self, substitute=..., descend_into_named_expressions=..., remove_named_expressions=...) -> None:
        ...
    
    def initializeWalker(self, expr): # -> tuple[Literal[False], Any | None] | tuple[Literal[True], Any]:
        ...
    
    def beforeChild(self, node, child, child_idx): # -> tuple[Literal[False], Any] | tuple[Literal[True], None]:
        ...
    
    def enterNode(self, node): # -> tuple[list[Any], list[Any]]:
        ...
    
    def acceptChildResult(self, node, data, child_result, child_idx):
        ...
    
    def exitNode(self, node, data):
        ...
    
    @deprecated("ExpressionReplacementVisitor: this walker has been ported " "to derive from StreamBasedExpressionVisitor.  " "dfs_postorder_stack() has been replaced with walk_expression()", version='6.2')
    def dfs_postorder_stack(self, expr): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
        ...
    


def evaluate_fixed_subexpressions(expr, descend_into_named_expressions=..., remove_named_expressions=...): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
    ...

class EvaluateFixedSubexpressionVisitor(ExpressionReplacementVisitor):
    def __init__(self, descend_into_named_expressions=..., remove_named_expressions=...) -> None:
        ...
    
    def beforeChild(self, node, child, child_idx): # -> tuple[Literal[False], Any] | tuple[Literal[True], None]:
        ...
    


def clone_expression(expr, substitute=...): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
    """A function that is used to clone an expression.

    Cloning is equivalent to calling ``copy.deepcopy`` with no Block
    scope.  That is, the expression tree is duplicated, but no Pyomo
    components (leaf nodes *or* named Expressions) are duplicated.

    Args:
        expr: The expression that will be cloned.
        substitute (dict): A dictionary mapping object ids to
            objects. This dictionary has the same semantics as
            the memo object used with ``copy.deepcopy``. Defaults
            to None, which indicates that no user-defined
            dictionary is used.

    Returns:
        The cloned expression.

    """
    ...

def sizeof_expression(expr): # -> tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[()] | int | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[Any | tuple[Any | tuple[()] | int, ...] | tuple[()] | int, ...] | tuple[()] | int, ...] | list[Any] | None, ...] | list[Any] | Any | None:
    """
    Return the number of nodes in the expression tree.

    Args:
        expr: The root node of an expression tree.

    Returns:
        A non-negative integer that is the number of
        interior and leaf nodes in the expression tree.
    """
    ...

class _EvaluationVisitor(ExpressionValueVisitor):
    def __init__(self, exception) -> None:
        ...
    
    def visit(self, node, values):
        """Visit nodes that have been expanded"""
        ...
    
    def visiting_potential_leaf(self, node): # -> tuple[Literal[True], Any] | tuple[Literal[False], None] | tuple[Literal[True], Any | None]:
        """
        Visiting a potential leaf.

        Return True if the node is not expanded.
        """
        ...
    


class FixedExpressionError(Exception):
    def __init__(self, *args, **kwds) -> None:
        ...
    


class NonConstantExpressionError(Exception):
    def __init__(self, *args, **kwds) -> None:
        ...
    


class _EvaluateConstantExpressionVisitor(ExpressionValueVisitor):
    def visit(self, node, values):
        """Visit nodes that have been expanded"""
        ...
    
    def visiting_potential_leaf(self, node): # -> tuple[Literal[True], Any] | tuple[Literal[False], None] | tuple[Literal[True], Any | None]:
        """
        Visiting a potential leaf.

        Return True if the node is not expanded.
        """
        ...
    


def evaluate_expression(exp, exception=..., constant=...): # -> Any | None:
    """Evaluate the value of the expression.

    Args:
        expr: The root node of an expression tree.
        exception (bool): A flag that indicates whether
            exceptions are raised.  If this flag is
            :const:`False`, then an exception that
            occurs while evaluating the expression
            is caught and the return value is :const:`None`.
            Default is :const:`True`.
        constant (bool): If True, constant expressions are
            evaluated and returned but nonconstant expressions
            raise either FixedExpressionError or
            NonconstantExpressionError (default=False).

    Returns:
        A floating point value if the expression evaluates
        normally, or :const:`None` if an exception occurs
        and is caught.

    """
    ...

class _ComponentVisitor(SimpleExpressionVisitor):
    def __init__(self, types) -> None:
        ...
    
    def visit(self, node): # -> None:
        ...
    


def identify_components(expr, component_types): # -> Generator[Never, Any, None]:
    """
    A generator that yields a sequence of nodes
    in an expression tree that belong to a specified set.

    Args:
        expr: The root node of an expression tree.
        component_types (set or list): A set of class
            types that will be matched during the search.

    Yields:
        Each node that is found.
    """
    ...

class _VariableVisitor(StreamBasedExpressionVisitor):
    def __init__(self, include_fixed=..., named_expression_cache=...) -> None:
        """Visitor that collects all unique variables participating in an
        expression

        Args:
            include_fixed (bool): Whether to include fixed variables
            named_expression_cache (optional, dict): Dict mapping ids of named
                expressions to a tuple of the list of all variables and the
                set of all variable ids contained in the named expression.

        """
        ...
    
    def initializeWalker(self, expr): # -> tuple[Literal[False], list[Any]] | tuple[Literal[False], Any] | tuple[Literal[True], Any]:
        ...
    
    def beforeChild(self, parent, child, index): # -> tuple[Literal[False], None] | tuple[Literal[True], None]:
        ...
    
    def exitNode(self, node, data): # -> None:
        ...
    
    def finalizeResult(self, result): # -> list[Any]:
        ...
    


def identify_variables(expr, include_fixed=..., named_expression_cache=...): # -> Generator[Any, Any, None]:
    """
    A generator that yields a sequence of variables
    in an expression tree.

    Args:
        expr: The root node of an expression tree.
        include_fixed (bool): If :const:`True`, then
            this generator will yield variables whose
            value is fixed.  Defaults to :const:`True`.

    Yields:
        Each variable that is found.
    """
    ...

class _MutableParamVisitor(SimpleExpressionVisitor):
    def __init__(self) -> None:
        ...
    
    def visit(self, node): # -> None:
        ...
    


def identify_mutable_parameters(expr): # -> Generator[Never, Any, None]:
    """
    A generator that yields a sequence of mutable
    parameters in an expression tree.

    Args:
        expr: The root node of an expression tree.

    Yields:
        Each mutable parameter that is found.
    """
    ...

class _PolynomialDegreeVisitor(ExpressionValueVisitor):
    def visit(self, node, values):
        """Visit nodes that have been expanded"""
        ...
    
    def visiting_potential_leaf(self, node): # -> tuple[Literal[True], Literal[0]] | tuple[Literal[False], None] | tuple[Literal[True], Literal[0, 1]] | tuple[Literal[True], Any]:
        """
        Visiting a potential leaf.

        Return True if the node is not expanded.
        """
        ...
    


def polynomial_degree(node):
    """
    Return the polynomial degree of the expression.

    Args:
        node: The root node of an expression tree.

    Returns:
        A non-negative integer that is the polynomial
        degree if the expression is polynomial, or :const:`None` otherwise.
    """
    ...

class _IsFixedVisitor(ExpressionValueVisitor):
    """
    NOTE: This doesn't check if combiner logic is
    all or any and short-circuit the test.  It's
    not clear that that is an important optimization.
    """
    def visit(self, node, values):
        """Visit nodes that have been expanded"""
        ...
    
    def visiting_potential_leaf(self, node): # -> tuple[Literal[True], Literal[True]] | tuple[Literal[False], None] | tuple[Literal[True], Any]:
        """
        Visiting a potential leaf.

        Return True if the node is not expanded.
        """
        ...
    


LEFT_TO_RIGHT = ...
RIGHT_TO_LEFT = ...
class _ToStringVisitor(ExpressionValueVisitor):
    _expression_handlers = ...
    _leaf_node_types = ...
    def __init__(self, verbose, smap) -> None:
        ...
    
    def visit(self, node, values):
        """Visit nodes that have been expanded"""
        ...
    
    def visiting_potential_leaf(self, node): # -> tuple[Literal[True], None] | tuple[Literal[True], str] | tuple[Literal[False], None] | tuple[Literal[True], Any]:
        """
        Visiting a potential leaf.

        Return True if the node is not expanded.
        """
        ...
    


def expression_to_string(expr, verbose=..., labeler=..., smap=..., compute_values=...):
    """Return a string representation of an expression.

    Parameters
    ----------
    expr: ExpressionBase
        The root node of an expression tree.

    verbose: bool
        If :const:`True`, then the output is a nested functional form.
        Otherwise, the output is an algebraic expression.  Default is
        retrieved from :py:attr:`common.TO_STRING_VERBOSE`

    labeler: Callable
        If specified, this labeler is used to generate the string
        representation for leaves (Var / Param objects) in the
        expression.

    smap:  SymbolMap
        If specified, this :class:`SymbolMap
        <pyomo.core.expr.symbol_map.SymbolMap>` is used to cache labels.

    compute_values: bool
        If :const:`True`, then parameters and fixed variables are
        evaluated before the expression string is generated.  Default is
        :const:`False`.

    Returns:
        A string representation for the expression.

    """
    ...
