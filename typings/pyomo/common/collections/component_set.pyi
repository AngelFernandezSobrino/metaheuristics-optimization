"""
This type stub file was generated by pyright.
"""

from collections.abc import MutableSet as collections_MutableSet
from pyomo.common.autoslots import AutoSlots

class ComponentSet(AutoSlots.Mixin, collections_MutableSet):
    """
    This class is a replacement for set that allows Pyomo
    modeling components to be used as entries. The
    underlying hash is based on the Python id() of the
    object, which gets around the problem of hashing
    subclasses of NumericValue. This class is meant for
    creating sets of Pyomo components. The use of non-Pyomo
    components as entries should be avoided (as the behavior
    is undefined).

    References to objects are kept around as long as they
    are entries in the container, so there is no need to
    worry about id() clashes.

    We also override __setstate__ so that we can rebuild the
    container based on possibly updated object ids after
    a deepcopy or pickle.

    *** An instance of this class should never be
    deepcopied/pickled unless it is done so along with
    its component entries (e.g., as part of a block). ***
    """
    __slots__ = ...
    __autoslot_mappers__ = ...
    hasher = ...
    def __init__(self, iterable=...) -> None:
        ...
    
    def __str__(self) -> str:
        """String representation of the mapping."""
        ...
    
    def update(self, iterable): # -> None:
        """Update a set with the union of itself and others."""
        ...
    
    def __contains__(self, val): # -> bool:
        ...
    
    def __iter__(self): # -> Iterator[Any]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def add(self, val): # -> None:
        """Add an element."""
        ...
    
    def discard(self, val): # -> None:
        """Remove an element. Do not raise an exception if absent."""
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def clear(self): # -> None:
        """Remove all elements from this set."""
        ...
    
    def remove(self, val): # -> None:
        """Remove an element. If not a member, raise a KeyError."""
        ...
    

