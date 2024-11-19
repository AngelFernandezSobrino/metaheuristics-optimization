"""
This type stub file was generated by pyright.
"""

from pyomo.solvers.plugins.solvers.direct_or_persistent_solver import DirectOrPersistentSolver

logger = ...
class DirectSolver(DirectOrPersistentSolver):
    """
    Subclasses need to:
    1.) Initialize self._solver_model during _presolve before calling DirectSolver._presolve
    """
    def solve(self, *args, **kwds):
        """Solve the problem"""
        ...
    


