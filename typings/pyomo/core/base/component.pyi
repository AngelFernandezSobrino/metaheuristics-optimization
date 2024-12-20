"""
This type stub file was generated by pyright.
"""

import pyomo.common
from pyomo.common.deprecation import RenamedClass, deprecated
from pyomo.common.factory import Factory
from pyomo.core.pyomoobject import PyomoObject

logger = ...
_ref_types = ...
class ModelComponentFactoryClass(Factory):
    def register(self, doc=...): # -> Callable[..., Any]:
        ...
    


ModelComponentFactory = ...
def name(component, index=..., fully_qualified=..., relative_to=...):
    """
    Return a string representation of component for a specific
    index value.
    """
    ...

@deprecated(msg="The cname() function has been renamed to name()", version='5.6.9')
def cname(*args, **kwds):
    ...

class CloneError(pyomo.common.errors.PyomoException):
    ...


class ComponentBase(PyomoObject):
    """A base class for Component and ComponentData

    This class defines some fundamental methods and properties that are
    expected for all Component-like objects.  They are centralized here
    to avoid repeated code in the Component and ComponentData classes.
    """
    __slots__ = ...
    _PPRINT_INDENT = ...
    def is_component_type(self): # -> Literal[True]:
        """Return True if this class is a Pyomo component"""
        ...
    
    def __deepcopy__(self, memo): # -> Self:
        ...
    
    def __deepcopy_field__(self, value, memo, slot_name): # -> None:
        ...
    
    @deprecated("""The cname() method has been renamed to getname().
    The preferred method of obtaining a component name is to use the
    .name property, which returns the fully qualified component name.
    The .local_name property will return the component name only within
    the context of the immediate parent container.""", version='5.0')
    def cname(self, *args, **kwds):
        ...
    
    def pprint(self, ostream=..., verbose=..., prefix=...): # -> None:
        """Print component information

        Note that this method is generally only reachable through
        ComponentData objects in an IndexedComponent container.
        Components, including unindexed Component derivatives and both
        scalar and indexed IndexedComponent derivatives will see
        :py:meth:`Component.pprint()`
        """
        ...
    
    @property
    def name(self):
        """Get the fully qualified component name."""
        ...
    
    @name.setter
    def name(self, val):
        ...
    
    @property
    def local_name(self):
        """Get the component name only within the context of
        the immediate parent container."""
        ...
    
    @property
    def active(self): # -> Literal[True]:
        """Return the active attribute"""
        ...
    
    @active.setter
    def active(self, value):
        """Set the active attribute to the given value"""
        ...
    


class _ComponentBase(metaclass=RenamedClass):
    __renamed__new_class__ = ComponentBase
    __renamed__version__ = ...


class Component(ComponentBase):
    """
    This is the base class for all Pyomo modeling components.

    Parameters
    ----------
    ctype : type
        The class type for the derived subclass

    doc : str
        A text string describing this component

    name : str
        A name for this component

    Attributes
    ----------
    doc : str
        A text string describing this component

    """
    __autoslot_mappers__ = ...
    def __init__(self, **kwds) -> None:
        ...
    
    @property
    def ctype(self):
        """Return the class type for this component"""
        ...
    
    @deprecated("Component.type() method has been replaced by the .ctype property.", version='5.7')
    def type(self):
        """Return the class type for this component"""
        ...
    
    def construct(self, data=...): # -> None:
        """API definition for constructing components"""
        ...
    
    def is_constructed(self): # -> bool:
        """Return True if this class has been constructed"""
        ...
    
    def reconstruct(self, data=...):
        """REMOVED: reconstruct() was removed in Pyomo 6.0.

        Re-constructing model components was fragile and did not
        correctly update instances of the component used in other
        components or contexts (this was particularly problemmatic for
        Var, Param, and Set).  Users who wish to reproduce the old
        behavior of reconstruct(), are comfortable manipulating
        non-public interfaces, and who take the time to verify that the
        correct thing happens to their model can approximate the old
        behavior of reconstruct with:

            component.clear()
            component._constructed = False
            component.construct()

        """
        ...
    
    def valid_model_component(self): # -> Literal[True]:
        """Return True if this can be used as a model component."""
        ...
    
    def pprint(self, ostream=..., verbose=..., prefix=...): # -> None:
        """Print component information"""
        ...
    
    def display(self, ostream=..., verbose=..., prefix=...): # -> None:
        ...
    
    def parent_component(self): # -> Self:
        """Returns the component associated with this object."""
        ...
    
    def parent_block(self): # -> None:
        """Returns the parent of this object."""
        ...
    
    def model(self): # -> None:
        """Returns the model associated with this object."""
        ...
    
    def root_block(self): # -> None:
        """Return self.model()"""
        ...
    
    def __str__(self) -> str:
        """Return the component name"""
        ...
    
    def getname(self, fully_qualified=..., name_buffer=..., relative_to=...): # -> str:
        """Returns the component name associated with this object.

        Parameters
        ----------
        fully_qualified: bool
            Generate full name from nested block names

        relative_to: Block
            Generate fully_qualified names relative to the specified block.
        """
        ...
    
    @property
    def name(self): # -> str:
        """Get the fully qualified component name."""
        ...
    
    @name.setter
    def name(self, val): # -> None:
        ...
    
    def is_indexed(self): # -> Literal[False]:
        """Return true if this component is indexed"""
        ...
    
    def clear_suffix_value(self, suffix_or_name, expand=...): # -> None:
        """Clear the suffix value for this component data"""
        ...
    
    def set_suffix_value(self, suffix_or_name, value, expand=...): # -> None:
        """Set the suffix value for this component data"""
        ...
    
    def get_suffix_value(self, suffix_or_name, default=...): # -> None:
        """Get the suffix value for this component data"""
        ...
    


class ActiveComponent(Component):
    """A Component that makes semantic sense to activate or deactivate
    in a model.

    Private class attributes:
        _active         A boolean that is true if this component will be
                            used in model operations
    """
    def __init__(self, **kwds) -> None:
        ...
    
    @property
    def active(self): # -> bool:
        """Return the active attribute"""
        ...
    
    @active.setter
    def active(self, value):
        """Set the active attribute to the given value"""
        ...
    
    def activate(self): # -> None:
        """Set the active attribute to True"""
        ...
    
    def deactivate(self): # -> None:
        """Set the active attribute to False"""
        ...
    


class ComponentData(ComponentBase):
    """
    This is the base class for the component data used
    in Pyomo modeling components.  Subclasses of ComponentData are
    used in indexed components, and this class assumes that indexed
    components are subclasses of IndexedComponent.  Note that
    ComponentData instances do not store their index.  This makes
    some operations significantly more expensive, but these are (a)
    associated with I/O generation and (b) this cost can be managed
    with caches.

    Constructor arguments:
        owner           The component that owns this data object

    Private class attributes:
        _component      A weakref to the component that owns this data object
        _index          The index of this data object
    """
    __slots__ = ...
    __autoslot_mappers__ = ...
    def __init__(self, component) -> None:
        ...
    
    @property
    def ctype(self): # -> None:
        """Return the class type for this component"""
        ...
    
    @deprecated("Component.type() method has been replaced by the .ctype property.", version='5.7')
    def type(self): # -> None:
        """Return the class type for this component"""
        ...
    
    def parent_component(self): # -> Any | None:
        """Returns the component associated with this object."""
        ...
    
    def parent_block(self): # -> None:
        """Return the parent of the component that owns this data."""
        ...
    
    def model(self): # -> None:
        """Return the model of the component that owns this data."""
        ...
    
    def index(self): # -> type[NOTSET]:
        """
        Returns the index of this ComponentData instance relative
        to the parent component index set. None is returned if
        this instance does not have a parent component, or if
        - for some unknown reason - this instance does not belong
        to the parent component's index set.
        """
        ...
    
    def __str__(self) -> str:
        """Return a string with the component name and index"""
        ...
    
    def getname(self, fully_qualified=..., name_buffer=..., relative_to=...): # -> str:
        """Return a string with the component name and index"""
        ...
    
    def is_indexed(self): # -> Literal[False]:
        """Return true if this component is indexed"""
        ...
    
    def clear_suffix_value(self, suffix_or_name, expand=...): # -> None:
        """Set the suffix value for this component data"""
        ...
    
    def set_suffix_value(self, suffix_or_name, value, expand=...): # -> None:
        """Set the suffix value for this component data"""
        ...
    
    def get_suffix_value(self, suffix_or_name, default=...): # -> None:
        """Get the suffix value for this component data"""
        ...
    


class ActiveComponentData(ComponentData):
    """
    This is the base class for the component data used
    in Pyomo modeling components that can be activated and
    deactivated.

    It's possible to end up in a state where the parent Component
    has _active=True but all ComponentData have _active=False. This
    seems like a reasonable state, though we cannot easily detect
    this situation.  The important thing to avoid is the situation
    where one or more ComponentData are active, but the parent
    Component claims active=False. This class structure is designed
    to prevent this situation.

    Constructor arguments:
        owner           The component that owns this data object

    Private class attributes:
        _component      A weakref to the component that owns this data object
        _index          The index of this data object
        _active         A boolean that indicates whether this data is active
    """
    __slots__ = ...
    def __init__(self, component) -> None:
        ...
    
    @property
    def active(self): # -> bool:
        """Return the active attribute"""
        ...
    
    @active.setter
    def active(self, value):
        """Set the active attribute to a specified value."""
        ...
    
    def activate(self): # -> None:
        """Set the active attribute to True"""
        ...
    
    def deactivate(self): # -> None:
        """Set the active attribute to False"""
        ...
    


