"""
This type stub file was generated by pyright.
"""

"""
Utilities to support the definition of optimization applications that
can be optimized with the Acro COLIN optimizers.
"""
class AmplModel:
    """
    A class that provides a wrapper for AMPL models.
    """
    def __init__(self, modfile, datfile=...) -> None:
        """
        The constructor.
        """
        ...
    
    def valid_problem_types(self): # -> list[ProblemFormat]:
        """This method allows the pyomo.opt convert function to work with an AmplModel object."""
        ...
    
    def write(self, filename, format=..., solver_capability=...): # -> None:
        """
        Write the model to a file, with a given format.

        NOTE: this is the same exact code as is used in PyomoModel.py
        """
        ...
    

