"""
This type stub file was generated by pyright.
"""

from pyomo.common.autoslots import AutoSlots

initializer_map = ...
sequence_types = ...
function_types = ...
def Initializer(arg, allow_generators=..., treat_sequences_as_mappings=..., arg_not_specified=..., additional_args=...):
    """Standardized processing of Component keyword arguments

    Component keyword arguments accept a number of possible inputs, from
    scalars to dictionaries, to functions (rules) and generators.  This
    function standardizes the processing of keyword arguments and
    returns "initializer classes" that are specialized to the specific
    data type provided.

    Parameters
    ----------
    arg:

        The argument passed to the component constructor.  This could
        be almost any type, including a scalar, dict, list, function,
        generator, or None.

    allow_generators: bool

        If False, then we will raise an exception if ``arg`` is a generator

    treat_sequences_as_mappings: bool

        If True, then if ``arg`` is a sequence, we will treat it as if
        it were a mapping (i.e., ``dict(enumerate(arg))``).  Otherwise
        sequences will be returned back as the value of the initializer.

    arg_not_specified:

        If ``arg`` is ``arg_not_specified``, then the function will
        return None (and not an InitializerBase object).

    additional_args: int

        The number of additional arguments that will be passed to any
        function calls (provided *before* the index value).

    """
    ...

class InitializerBase(AutoSlots.Mixin):
    """Base class for all Initializer objects"""
    __slots__ = ...
    verified = ...
    def constant(self): # -> Literal[False]:
        """Return True if this initializer is constant across all indices"""
        ...
    
    def contains_indices(self): # -> Literal[False]:
        """Return True if this initializer contains embedded indices"""
        ...
    
    def indices(self):
        """Return a generator over the embedded indices

        This will raise a RuntimeError if this initializer does not
        contain embedded indices
        """
        ...
    


class ConstantInitializer(InitializerBase):
    """Initializer for constant values"""
    __slots__ = ...
    def __init__(self, val) -> None:
        ...
    
    def __call__(self, parent, idx): # -> Any:
        ...
    
    def constant(self): # -> Literal[True]:
        ...
    


class ItemInitializer(InitializerBase):
    """Initializer for dict-like values supporting __getitem__()"""
    __slots__ = ...
    def __init__(self, _dict) -> None:
        ...
    
    def __call__(self, parent, idx):
        ...
    
    def contains_indices(self): # -> Literal[True]:
        ...
    
    def indices(self): # -> range:
        ...
    


class DataFrameInitializer(InitializerBase):
    """Initializer for pandas DataFrame values"""
    __slots__ = ...
    def __init__(self, dataframe, column=...) -> None:
        ...
    
    def __call__(self, parent, idx):
        ...
    
    def contains_indices(self): # -> Literal[True]:
        ...
    
    def indices(self):
        ...
    


class IndexedCallInitializer(InitializerBase):
    """Initializer for functions and callable objects"""
    __slots__ = ...
    def __init__(self, _fcn) -> None:
        ...
    
    def __call__(self, parent, idx):
        ...
    


class ParameterizedIndexedCallInitializer(IndexedCallInitializer):
    """IndexedCallInitializer that accepts additional arguments"""
    __slots__ = ...
    def __call__(self, parent, idx, *args):
        ...
    


class CountedCallGenerator:
    """Generator implementing the "counted call" initialization scheme

    This generator implements the older "counted call" scheme, where the
    first argument past the parent block is a monotonically-increasing
    integer beginning at `start_at`.
    """
    def __init__(self, ctype, fcn, scalar, parent, idx, start_at) -> None:
        ...
    
    def __iter__(self): # -> Self:
        ...
    
    def __next__(self):
        ...
    
    next = ...


class CountedCallInitializer(InitializerBase):
    """Initializer for functions implementing the "counted call" API."""
    __slots__ = ...
    def __init__(self, obj, _indexed_init, starting_index=...) -> None:
        ...
    
    def __call__(self, parent, idx): # -> CountedCallGenerator:
        ...
    


class ScalarCallInitializer(InitializerBase):
    """Initializer for functions taking only the parent block argument."""
    __slots__ = ...
    def __init__(self, _fcn, constant=...) -> None:
        ...
    
    def __call__(self, parent, idx):
        ...
    
    def constant(self): # -> bool:
        """Return True if this initializer is constant across all indices"""
        ...
    


class ParameterizedScalarCallInitializer(ScalarCallInitializer):
    """ScalarCallInitializer that accepts additional arguments"""
    __slots__ = ...
    def __call__(self, parent, idx, *args):
        ...
    


class DefaultInitializer(InitializerBase):
    """Initializer wrapper that maps exceptions to default values.


    Parameters
    ----------
    initializer: :py:class`InitializerBase`
        the Initializer instance to wrap

    default:
        the value to return inlieu of the caught exception(s)

    exceptions: Exception or tuple
        the single Exception or tuple of Exceptions to catch and return
        the default value.

    """
    __slots__ = ...
    def __init__(self, initializer, default, exceptions) -> None:
        ...
    
    def __call__(self, parent, index): # -> Any:
        ...
    
    def constant(self):
        """Return True if this initializer is constant across all indices"""
        ...
    
    def contains_indices(self):
        """Return True if this initializer contains embedded indices"""
        ...
    
    def indices(self):
        ...
    


class ParameterizedInitializer(InitializerBase):
    """Base class for all Initializer objects"""
    __slots__ = ...
    def __init__(self, base) -> None:
        ...
    
    def constant(self):
        """Return True if this initializer is constant across all indices"""
        ...
    
    def contains_indices(self):
        """Return True if this initializer contains embedded indices"""
        ...
    
    def indices(self):
        """Return a generator over the embedded indices

        This will raise a RuntimeError if this initializer does not
        contain embedded indices
        """
        ...
    
    def __call__(self, parent, idx, *args):
        ...
    


_bound_sequence_types = ...
class BoundInitializer(InitializerBase):
    """Initializer wrapper for processing bounds (mapping scalars to 2-tuples)

    Note that this class is meant to mimic the behavior of
    :py:func:`Initializer` and will return ``None`` if the initializer
    that it is wrapping is ``None``.

    Parameters
    ----------
    arg:

        As with :py:func:`Initializer`, this is the raw argument passed
        to the component constructor.

    obj: :py:class:`Component`

        The component that "owns" the initializer.  This initializer
        will treat sequences as mappings only if the owning component is
        indexed and the sequence passed to the initializer is not of
        length 2

    """
    __slots__ = ...
    def __new__(cls, arg=..., obj=...): # -> Self | None:
        ...
    
    def __init__(self, arg, obj=...) -> None:
        ...
    
    def __call__(self, parent, index): # -> str | Sequence[Any] | tuple[Any | str | Sequence[Any], Any | str | Sequence[Any]]:
        ...
    
    def constant(self):
        """Return True if this initializer is constant across all indices"""
        ...
    
    def contains_indices(self):
        """Return True if this initializer contains embedded indices"""
        ...
    
    def indices(self):
        ...
    


