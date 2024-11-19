"""
This type stub file was generated by pyright.
"""

"""This module provides general utilities for producing formatted I/O

.. autosummary::

   tostr
   tabular_writer
   wrap_reStructuredText
   StreamIndenter
"""
def tostr(value, quote_str=...): # -> Any:
    """Convert a value to a string

    This function is a thin wrapper around `str(value)` to resolve a
    problematic __str__ implementation in the standard Python container
    types (tuple, list, and dict).  Those classes implement __str__ the
    same as __repr__ (by calling repr() on each contained object).  That
    is frequently undesirable, as you may wish the string representation
    of a container to contain the string representations of the
    contained objects.

    This function generates string representations for native Python
    containers (tuple, list, and dict) that contains the string
    representations of the contained objects.  In addition, it also
    applies the same special handling to any types that derive from the
    standard containers without overriding either __repn__ or __str__.

    Parameters
    ----------
    value: object
        the object to convert to a string
    quote_str: bool
        if True, and if `value` is a `str`, then return a "quoted
        string" (as generated by repr()).  This is primarily used when
        recursively processing native Python containers.

    Returns
    -------
    str

    """
    ...

def tabular_writer(ostream, prefix, data, header, row_generator): # -> None:
    """Output data in tabular form

    Parameters
    ----------
    ostream: io.TextIOBase
        the stream to write to
    prefix: str
        prefix each generated line with this string
    data: iterable
        an iterable object that returns (key, value) pairs
        (e.g., from iteritems()) defining each row in the table
    header: List[str]
        list of column headers
    row_generator: function
        a function that accepts the `key` and `value` from `data` and
        returns either a tuple defining the entries for a single row, or
        a generator that returns a sequence of table rows to be output
        for the specified `key`

    """
    ...

class StreamIndenter:
    """
    Mock-up of a file-like object that wraps another file-like object
    and indents all data using the specified string before passing it to
    the underlying file.  Since this presents a full file interface,
    StreamIndenter objects may be arbitrarily nested.
    """
    def __init__(self, ostream, indent=...) -> None:
        ...
    
    def __getattr__(self, name): # -> Any:
        ...
    
    def write(self, data): # -> None:
        ...
    
    def writelines(self, sequence): # -> None:
        ...
    


_indentation_re = ...
_bullet_re = ...
_verbatim_line_start = ...
_verbatim_line = ...
def wrap_reStructuredText(docstr, wrapper):
    """A text wrapper that honors paragraphs and basic reStructuredText markup

    This wraps `textwrap.fill()` to first separate the incoming text by
    paragraphs before using ``wrapper`` to wrap each one.  It includes a
    basic (partial) parser for reStructuredText format to attempt to
    avoid wrapping structural elements like section headings, bullet /
    enumerated lists, and tables.

    Parameters
    ----------
    docstr : str
        The incoming string to parse and wrap

    wrapper : `textwrap.TextWrap`
        The configured `TextWrap` object to use for wrapping paragraphs.
        While the object will be reconfigured within this function, it
        will be restored to its original state upon exit.

    """
    ...

