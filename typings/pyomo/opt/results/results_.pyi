"""
This type stub file was generated by pyright.
"""

from pyomo.opt.results.container import MapContainer, undefined

logger = ...
class SolverResults(MapContainer):
    undefined = ...
    default_print_options = ...
    def __init__(self) -> None:
        ...
    
    def add(self, name, value, active, description): # -> None:
        ...
    
    def json_repn(self, options=...): # -> UndefinedData | dict[Any, Any]:
        ...
    
    def write(self, **kwds): # -> None:
        ...
    
    def write_json(self, **kwds): # -> None:
        ...
    
    def write_yaml(self, **kwds): # -> None:
        ...
    
    def read(self, **kwds): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    


if __name__ == '__main__':
    results = ...
