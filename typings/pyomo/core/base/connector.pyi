"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import RenamedClass, deprecated
from pyomo.core.expr.numvalue import NumericValue
from pyomo.core.base.component import ComponentData, ModelComponentFactory
from pyomo.core.base.indexed_component import IndexedComponent

logger = ...
class ConnectorData(ComponentData, NumericValue):
    """Holds the actual connector information"""
    __slots__ = ...
    def __init__(self, component=...) -> None:
        """Constructor"""
        ...
    
    def set_value(self, value):
        ...
    
    def is_fixed(self): # -> bool:
        """Return True if all vars/expressions in the Connector are fixed"""
        ...
    
    def is_constant(self): # -> Literal[False]:
        """Return False

        Because the expression generation logic will attempt to evaluate
        constant subexpressions, a Connector can never be constant.
        """
        ...
    
    def is_potentially_variable(self): # -> Literal[True]:
        """Return True as connectors may (should!) contain variables"""
        ...
    
    def polynomial_degree(self): # -> int | None:
        ...
    
    def is_binary(self): # -> bool | Literal[0]:
        ...
    
    def is_integer(self): # -> bool | Literal[0]:
        ...
    
    def is_continuous(self): # -> bool | Literal[0]:
        ...
    
    def add(self, var, name=..., aggregate=...): # -> None:
        ...
    


class _ConnectorData(metaclass=RenamedClass):
    __renamed__new_class__ = ConnectorData
    __renamed__version__ = ...


@ModelComponentFactory.register("A bundle of variables that can be manipulated together.")
@deprecated("Use of pyomo.connectors is deprecated. " "Its functionality has been replaced by pyomo.network.", version='5.6.9')
class Connector(IndexedComponent):
    """A collection of variables, which may be defined over a index

    The idea behind a Connector is to create a bundle of variables that
    can be manipulated as a single variable within constraints.  While
    Connectors inherit from variable (mostly so that the expression
    infrastructure can manipulate them), they are not actual variables
    that are exposed to the solver.  Instead, a preprocessor
    (ConnectorExpander) will look for expressions that involve
    connectors and replace the single constraint with a list of
    constraints that involve the original variables contained within the
    Connector.

    Parameters
    ----------
    name : str
        The name of this connector

    index
        The index set that defines the distinct connectors.  By default,
        this is None, indicating that there is a single connector.

    """
    def __new__(cls, *args, **kwds): # -> Self:
        ...
    
    def __init__(self, *args, **kwd) -> None:
        ...
    
    def construct(self, data=...): # -> None:
        ...
    
    def display(self, prefix=..., ostream=...): # -> None:
        """
        Print component state information

        This duplicates logic in Component.pprint()
        """
        ...
    


class ScalarConnector(Connector, ConnectorData):
    def __init__(self, *args, **kwd) -> None:
        ...
    


class SimpleConnector(metaclass=RenamedClass):
    __renamed__new_class__ = ScalarConnector
    __renamed__version__ = ...


class IndexedConnector(Connector):
    """An array of connectors"""
    ...


