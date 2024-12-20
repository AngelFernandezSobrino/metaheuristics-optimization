"""
This type stub file was generated by pyright.
"""

WriterFactory = ...
class AbstractProblemWriter:
    """Base class that can write optimization problems."""
    def __init__(self, problem_format) -> None:
        ...
    
    def __call__(self, model, filename, solver_capability, **kwds):
        ...
    
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, t, v, traceback): # -> None:
        ...
    


class BranchDirection:
    """Allowed values for MIP variable branching directions in the `direction` Suffix of a model."""
    default = ...
    down = ...
    up = ...
    ALL = ...


