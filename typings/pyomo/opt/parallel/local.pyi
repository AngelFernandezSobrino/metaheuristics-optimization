"""
This type stub file was generated by pyright.
"""

from pyomo.opt.parallel.async_solver import AsynchronousSolverManager, SolverManagerFactory

@SolverManagerFactory.register("serial", doc="Synchronously execute solvers locally")
class SolverManager_Serial(AsynchronousSolverManager):
    def clear(self): # -> None:
        """
        Clear manager state
        """
        ...
    


