"""
This type stub file was generated by pyright.
"""

from pyomo.core.base.component import ModelComponentFactory
from pyomo.core.base.indexed_component import IndexedComponent

logger = ...
@ModelComponentFactory.register("A component that performs arbitrary actions during model construction.  " "The action rule is applied to every index value.")
class BuildAction(IndexedComponent):
    """A build action, which executes a rule for all valid indices.

    Constructor arguments:
        rule        The rule that is executed for every indice.

    Private class attributes:
        _rule       The rule that is executed for every indice.
    """
    def __init__(self, *args, **kwd) -> None:
        ...
    
    def construct(self, data=...): # -> None:
        """Apply the rule to construct values in this set"""
        ...
    


