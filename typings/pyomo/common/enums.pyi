"""
This type stub file was generated by pyright.
"""

import enum
import sys

"""This module provides standard :py:class:`enum.Enum` definitions used in
Pyomo, along with additional utilities for working with custom Enums

Utilities:

.. autosummary::

   ExtendedEnumType
   NamedIntEnum

Standard Enums:

.. autosummary::

   ObjectiveSense

"""
Enum = enum.Enum
if sys.version_info[: 2] < (3, 11):
    _EnumType = ...
else:
    _EnumType = enum.EnumType
if sys.version_info[: 2] < (3, 13):
    class IntEnum(enum.IntEnum):
        __doc__ = ...
        @_fix_doc(enum.IntEnum.to_bytes)
        def to_bytes(self, /, length=..., byteorder=..., *, signed=...): # -> bytes:
            ...
        
        @classmethod
        @_fix_doc(enum.IntEnum.from_bytes)
        def from_bytes(cls, bytes, byteorder=..., *, signed=...): # -> IntEnum:
            ...
        
    
    
else:
    IntEnum = ...
class ExtendedEnumType(_EnumType):
    """Metaclass for creating an :py:class:`enum.Enum` that extends another Enum

    In general, :py:class:`enum.Enum` classes are not extensible: that is,
    they are frozen when defined and cannot be the base class of another
    Enum.  This Metaclass provides a workaround for creating a new Enum
    that extends an existing enum.  Members in the base Enum are all
    present as members on the extended enum.

    Example
    -------

    .. testcode::
       :hide:

       import enum
       from pyomo.common.enums import ExtendedEnumType

    .. testcode::

       class ObjectiveSense(enum.IntEnum):
           minimize = 1
           maximize = -1

       class ProblemSense(enum.IntEnum, metaclass=ExtendedEnumType):
           __base_enum__ = ObjectiveSense

           unknown = 0

    .. doctest::

       >>> list(ProblemSense)
       [<ProblemSense.unknown: 0>, <ObjectiveSense.minimize: 1>, <ObjectiveSense.maximize: -1>]
       >>> ProblemSense.unknown
       <ProblemSense.unknown: 0>
       >>> ProblemSense.maximize
       <ObjectiveSense.maximize: -1>
       >>> ProblemSense(0)
       <ProblemSense.unknown: 0>
       >>> ProblemSense(1)
       <ObjectiveSense.minimize: 1>
       >>> ProblemSense('unknown')
       <ProblemSense.unknown: 0>
       >>> ProblemSense('maximize')
       <ObjectiveSense.maximize: -1>
       >>> hasattr(ProblemSense, 'minimize')
       True
       >>> ProblemSense.minimize is ObjectiveSense.minimize
       True
       >>> ProblemSense.minimize in ProblemSense
       True

    """
    def __getattr__(cls, attr): # -> Any:
        ...
    
    def __iter__(cls): # -> chain[ExtendedEnumType]:
        ...
    
    def __contains__(cls, member): # -> bool:
        ...
    
    def __instancecheck__(cls, instance): # -> Any | Literal[True]:
        ...
    
    def __new__(metacls, cls, bases, classdict, **kwds): # -> Self:
        ...
    


class NamedIntEnum(IntEnum):
    """An extended version of :py:class:`~pyomo.common.enums.IntEnum` that supports
    creating members by name as well as value.

    """
    ...


class ObjectiveSense(NamedIntEnum):
    """Flag indicating if an objective is minimizing (1) or maximizing (-1).

    While the numeric values are arbitrary, there are parts of Pyomo
    that rely on this particular choice of value.  These values are also
    consistent with some solvers (notably Gurobi).

    """
    minimize = ...
    maximize = ...
    def __str__(self) -> str:
        ...
    


minimize = ...
maximize = ...