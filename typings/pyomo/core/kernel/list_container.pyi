"""
This type stub file was generated by pyright.
"""

import collections.abc
from pyomo.core.kernel.tuple_container import TupleContainer

logger = ...
class ListContainer(TupleContainer, collections.abc.MutableSequence):
    """
    A partial implementation of the IHomogeneousContainer
    interface that provides list-like storage functionality.

    Complete implementations need to set the _ctype property
    at the class level and initialize the remaining
    ICategorizedObject attributes during object creation. If
    using __slots__, a slot named "_data" must be included.

    Note that this implementation allows nested storage of
    other ICategorizedObjectContainer implementations that
    are defined with the same ctype.
    """
    __slots__ = ...
    def __init__(self, *args) -> None:
        ...
    
    def __setitem__(self, i, item): # -> None:
        ...
    
    def insert(self, i, item): # -> None:
        """S.insert(index, object) -- insert object before index"""
        ...
    
    def __delitem__(self, i): # -> None:
        ...
    
    def reverse(self): # -> None:
        """S.reverse() -- reverse *IN PLACE*"""
        ...
    

