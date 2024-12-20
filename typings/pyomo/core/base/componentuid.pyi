"""
This type stub file was generated by pyright.
"""

import re
import ply.lex
from pyomo.common.deprecation import deprecated
from pyomo.core.base.component_namer import re_number as _re_number, special_chars

class _NotSpecified:
    ...


class ComponentUID:
    """
    A Component unique identifier

    This class provides a system to generate "component unique
    identifiers".  Any component in a model can be described by a CUID,
    and from a CUID you can find the component.  An important feature of
    CUIDs is that they are relative to a model, so you can use a CUID
    generated on one model to find the equivalent component on another
    model.  This is especially useful when you clone a model and want
    to, for example, copy a variable value from the cloned model back to
    the original model.

    The CUID has a string representation that can specify a specific
    component or a group of related components through the use of index
    wildcards (* for a single element in the index, and ** for all
    indexes)
    """
    __slots__ = ...
    _lex = ...
    _repr_v1_map = ...
    def __init__(self, component, cuid_buffer=..., context=...) -> None:
        ...
    
    def __str__(self) -> str:
        "Return a 'nicely formatted' string representation of the CUID"
        ...
    
    __repr__ = ...
    def get_repr(self, version=...): # -> LiteralString | str:
        ...
    
    def __getstate__(self): # -> dict[str, Any]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def __hash__(self) -> int:
        """Return a deterministic hash for this ComponentUID"""
        ...
    
    def __lt__(self, other) -> bool:
        """Return True if this CUID <= the 'other' CUID

        This method defines a lexicographic sorting order for
        ComponentUID objects.  Nominally this is equivalent to sorting
        tuples or strings (elements are compared in order, with the
        first difference determining the ordering; longer tuples / lists
        are sorted after shorter ones).  This includes special handling
        for slice and ellipsis, where slice is sorted after any specific
        index, and ellipsis is sorted after everything else.

        Following Python 3 convention, this will raise a TypeError if
        `other` is not a ComponentUID.

        """
        ...
    
    def __le__(self, other) -> bool:
        "Return True if this CUID <= the 'other' CUID"
        ...
    
    def __gt__(self, other) -> bool:
        "Return True if this CUID > the 'other' CUID"
        ...
    
    def __ge__(self, other) -> bool:
        "Return True if this CUID >= the 'other' CUID"
        ...
    
    def __eq__(self, other) -> bool:
        """Return True if this CUID is exactly equal to `other`

        This will return False (and not raise an exception) if `other`
        is not a ComponentUID.
        """
        ...
    
    def __ne__(self, other) -> bool:
        """Return True if this CUID is not exactly equal to `other`

        This will return True (and not raise an exception) if `other`
        is not a ComponentUID.
        """
        ...
    
    @staticmethod
    def generate_cuid_string_map(block, ctype=..., descend_into=..., repr_version=...): # -> ComponentMap:
        ...
    
    @deprecated("ComponentUID.find_component() is deprecated. " "Use ComponentUID.find_component_on()", version='5.7.2')
    def find_component(self, block): # -> Any | None:
        ...
    
    def find_component_on(self, block): # -> Any | None:
        """
        Return the (unique) component in the block.  If the CUID contains
        a wildcard in the last component, then returns that component.  If
        there are wildcards elsewhere (or the last component was a partial
        slice), then returns a reference.  See also list_components below.
        """
        ...
    
    def list_components(self, block): # -> Generator[Any | None, Any, None]:
        "Generator returning all components matching this ComponentUID"
        ...
    
    def matches(self, component, context=...): # -> bool:
        """Return True if this ComponentUID matches specified component

        This is equivalent to:

            `component in ComponentSet(self.list_components())`
        """
        ...
    


_re_escape_sequences = ...
t_ignore = ...
tokens = ...
@ply.lex.TOKEN(_re_number.pattern + r'(?=[,\]])')
def t_NUMBER(t):
    ...

@ply.lex.TOKEN(r'[a-zA-Z_0-9][^' + re.escape(special_chars) + r']*')
def t_WORD(t):
    ...

_quoted_str = ...
_general_str = ...
@ply.lex.TOKEN(_general_str)
def t_STRING(t):
    ...

@ply.lex.TOKEN(r'\*{1,2}')
def t_STAR(t):
    ...

@ply.lex.TOKEN(r'\|b?(?:' + _general_str + ")")
def t_PICKLE(t):
    ...

def t_error(t):
    ...

