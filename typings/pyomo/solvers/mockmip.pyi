"""
This type stub file was generated by pyright.
"""

class MockMIP:
    """Methods used to create a mock MIP solver used for testing"""
    def __init__(self, mockdir) -> None:
        ...
    
    def create_command_line(self, executable, problem_files): # -> None:
        ...
    
    executable = ...
    def version(self): # -> tuple[float, ...] | tuple[int, ...] | tuple[*tuple[int, ...], Literal[0]] | None:
        ...
    

