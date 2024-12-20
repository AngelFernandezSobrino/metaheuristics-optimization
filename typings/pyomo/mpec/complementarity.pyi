"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import RenamedClass
from pyomo.core import Block
from pyomo.core.base.component import ModelComponentFactory
from pyomo.core.base.block import BlockData
from pyomo.core.base.disable_methods import disable_methods

logger = ...
ComplementarityTuple = ...
def complements(a, b): # -> ComplementarityTuple:
    """Return a named 2-tuple"""
    ...

class ComplementarityData(BlockData):
    def to_standard_form(self): # -> None:
        ...
    
    def set_value(self, cc): # -> None:
        """
        Add a complementarity condition with a specified index.
        """
        ...
    


class _ComplementarityData(metaclass=RenamedClass):
    __renamed__new_class__ = ComplementarityData
    __renamed__version__ = ...


@ModelComponentFactory.register("Complementarity conditions.")
class Complementarity(Block):
    _ComponentDataClass = ComplementarityData
    def __new__(cls, *args, **kwds): # -> Self:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def add(self, index, cc): # -> ComponentData | None:
        """
        Add a complementarity condition with a specified index.
        """
        ...
    


class ScalarComplementarity(ComplementarityData, Complementarity):
    def __init__(self, *args, **kwds) -> None:
        ...
    


class SimpleComplementarity(metaclass=RenamedClass):
    __renamed__new_class__ = ScalarComplementarity
    __renamed__version__ = ...


@disable_methods('add', 'set_value', 'to_standard_form')
class AbstractScalarComplementarity(ScalarComplementarity):
    ...


class AbstractSimpleComplementarity(metaclass=RenamedClass):
    __renamed__new_class__ = AbstractScalarComplementarity
    __renamed__version__ = ...


class IndexedComplementarity(Complementarity):
    ...


@ModelComponentFactory.register("A list of complementarity conditions.")
class ComplementarityList(IndexedComplementarity):
    """
    A complementarity component that represents a list of complementarity
    conditions.  Each condition can be indexed by its index, but when added
    an index value is not specified.
    """
    End = ...
    def __init__(self, **kwargs) -> None:
        """Constructor"""
        ...
    
    def add(self, expr): # -> ComponentData | None:
        """
        Add a complementarity condition with an implicit index.
        """
        ...
    
    def construct(self, data=...): # -> None:
        """
        Construct the expression(s) for this complementarity condition.
        """
        ...
    


