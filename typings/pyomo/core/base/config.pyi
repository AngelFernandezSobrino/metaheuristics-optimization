"""
This type stub file was generated by pyright.
"""

logger = ...
class _PyomoOptions:
    def __init__(self) -> None:
        ...
    
    def active_config(self): # -> ConfigBlock:
        ...
    
    def __getitem__(self, key):
        ...
    
    def get(self, key, default=...): # -> ConfigBase | ConfigDict | ConfigValue | None:
        ...
    
    def __setitem__(self, key, val): # -> None:
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> map[Any]:
        ...
    
    def __getattr__(self, name):
        ...
    
    def __setattr__(self, name, value): # -> None:
        ...
    
    def iterkeys(self): # -> map[Any]:
        ...
    
    def itervalues(self): # -> map[Any]:
        ...
    
    def iteritems(self): # -> Generator[tuple[Any, Any], Any, None]:
        ...
    
    def keys(self): # -> map[Any]:
        ...
    
    def values(self): # -> map[Any]:
        ...
    
    def items(self): # -> Generator[tuple[Any, Any], Any, None]:
        ...
    
    def declare(self, name, config):
        ...
    
    def add(self, name, config): # -> ConfigBase | ConfigValue | ConfigDict:
        ...
    
    def value(self, accessValue=...): # -> dict[Any, Any]:
        ...
    
    def set_value(self, value): # -> ConfigBlock:
        ...
    
    def reset(self): # -> None:
        ...
    


def default_pyomo_config(): # -> ConfigBlock:
    ...

PyomoOptions = ...