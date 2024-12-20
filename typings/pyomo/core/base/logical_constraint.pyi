"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import RenamedClass
from pyomo.core.base.component import ActiveComponentData, ModelComponentFactory
from pyomo.core.base.indexed_component import ActiveIndexedComponent

logger = ...
_rule_returned_none_error = ...
class LogicalConstraintData(ActiveComponentData):
    """
    This class defines the data for a single general logical constraint.

    Constructor arguments:
        component
            The LogicalStatement object that owns this data.
        expr
            The Pyomo expression stored in this logical constraint.

    Public class attributes:
        active
            A boolean that is true if this logical constraint is
            active in the model.
        expr
            The Pyomo expression for this logical constraint

    Private class attributes:
        _component
            The logical constraint component.
        _active
            A boolean that indicates whether this data is active

    """
    __slots__ = ...
    def __init__(self, expr=..., component=...) -> None:
        ...
    
    def __call__(self, exception=...): # -> None:
        """Compute the value of the body of this logical constraint."""
        ...
    
    @property
    def body(self): # -> BooleanConstant | None:
        """Access the body of a logical constraint expression."""
        ...
    
    @property
    def expr(self): # -> BooleanConstant | None:
        """Return the expression associated with this logical constraint."""
        ...
    
    def set_value(self, expr): # -> None:
        """Set the expression on this logical constraint."""
        ...
    
    def get_value(self): # -> BooleanConstant | None:
        """Get the expression on this logical constraint."""
        ...
    


class _LogicalConstraintData(metaclass=RenamedClass):
    __renamed__new_class__ = LogicalConstraintData
    __renamed__version__ = ...


class _GeneralLogicalConstraintData(metaclass=RenamedClass):
    __renamed__new_class__ = LogicalConstraintData
    __renamed__version__ = ...


@ModelComponentFactory.register("General logical constraints.")
class LogicalConstraint(ActiveIndexedComponent):
    """
    This modeling component defines a logical constraint using a
    rule function.

    Constructor arguments:
        expr
            A Pyomo expression for this logical constraint
        rule
            A function that is used to construct logical constraints
        doc
            A text string describing this component
        name
            A name for this component

    Public class attributes:
        doc
            A text string describing this component
        name
            A name for this component
        active
            A boolean that is true if this component will be used to
            construct a model instance
        rule
           The rule used to initialize the logical constraint(s)

    Private class attributes:
        _constructed
            A boolean that is true if this component has been constructed
        _data
            A dictionary from the index set to component data objects
        _index_set
            The set of valid indices
        _model
            A weakref to the model that owns this component
        _parent
            A weakref to the parent block that owns this component
        _type
            The class type for the derived subclass
    """
    _ComponentDataClass = LogicalConstraintData
    class Infeasible:
        ...
    
    
    Feasible = ActiveIndexedComponent.Skip
    NoConstraint = ActiveIndexedComponent.Skip
    Violated = Infeasible
    Satisfied = Feasible
    def __new__(cls, *args, **kwds): # -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def construct(self, data=...): # -> None:
        """
        Construct the expression(s) for this logical constraint.
        """
        ...
    
    def display(self, prefix=..., ostream=...): # -> None:
        """
        Print component state information

        This duplicates logic in Component.pprint()
        """
        ...
    


class ScalarLogicalConstraint(LogicalConstraintData, LogicalConstraint):
    """
    ScalarLogicalConstraint is the implementation representing a single,
    non-indexed logical constraint.
    """
    def __init__(self, *args, **kwds) -> None:
        ...
    
    @property
    def body(self): # -> Any:
        """Access the body of a logical constraint."""
        ...
    
    def set_value(self, expr): # -> None:
        """Set the expression on this logical constraint."""
        ...
    
    def add(self, index, expr): # -> Self:
        """Add a logical constraint with a given index."""
        ...
    


class SimpleLogicalConstraint(metaclass=RenamedClass):
    __renamed__new_class__ = ScalarLogicalConstraint
    __renamed__version__ = ...


class IndexedLogicalConstraint(LogicalConstraint):
    def add(self, index, expr): # -> Self | None:
        """Add a logical constraint with a given index."""
        ...
    


@ModelComponentFactory.register("A list of logical constraints.")
class LogicalConstraintList(IndexedLogicalConstraint):
    """
    A logical constraint component that represents a list of constraints.
    Constraints can be indexed by their index, but when they are
    added an index value is not specified.
    """
    End = ...
    def __init__(self, **kwargs) -> None:
        """Constructor"""
        ...
    
    def construct(self, data=...): # -> None:
        """
        Construct the expression(s) for this logical constraint.
        """
        ...
    
    def add(self, expr): # -> Self | None:
        """Add a logical constraint with an implicit index."""
        ...
    


