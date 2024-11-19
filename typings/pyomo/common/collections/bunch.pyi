"""
This type stub file was generated by pyright.
"""

class Bunch(dict):
    """A class that can be used to store a bunch of data dynamically.

    This class allows for unspecified attributes to have a default value
    of None.  This borrows the output formatting ideas from the
    ActiveState Code Container (recipe 496697).

    For historical reasons, attributes / keys are stored in the
    underlying dict unless they begin with an underscore, in which case
    they are stored as object attributes.

    """
    def __init__(self, *args, **kw) -> None:
        ...
    
    def update(self, d): # -> None:
        """
        The update is specialized for JSON-like data.  This
        recursively replaces dictionaries with Bunch objects.
        """
        ...
    
    def set_name(self, name): # -> None:
        ...
    
    def __getitem__(self, name): # -> Any:
        ...
    
    def __setitem__(self, name, val): # -> None:
        ...
    
    def __delitem__(self, name): # -> None:
        ...
    
    def __getattr__(self, name):
        ...
    
    def __setattr__(self, name, val): # -> None:
        ...
    
    def __delattr__(self, name): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self, nesting=..., indent=...) -> str:
        ...
    

