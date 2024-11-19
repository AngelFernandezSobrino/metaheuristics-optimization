"""
This type stub file was generated by pyright.
"""

from pyomo.solvers.plugins.solvers.direct_solver import DirectSolver
from pyomo.opt.base import SolverFactory

logger = ...
class DegreeError(ValueError):
    ...


@SolverFactory.register('gurobi_direct', doc='Direct python interface to Gurobi')
class GurobiDirect(DirectSolver):
    """A direct interface to Gurobi using gurobipy.

    :param manage_env: Set to True if this solver instance should create and
        manage its own Gurobi environment (defaults to False)
    :type manage_env: bool
    :param options: Dictionary of Gurobi parameters to set
    :type options: dict

    If ``manage_env`` is set to True, the ``GurobiDirect`` object creates a local
    Gurobi environment and manage all associated Gurobi resources. Importantly,
    this enables Gurobi licenses to be freed and connections terminated when the
    solver context is exited::

        with SolverFactory('gurobi', solver_io='python', manage_env=True) as opt:
            opt.solve(model)

        # All Gurobi models and environments are freed

    If ``manage_env`` is set to False (the default), the ``GurobiDirect`` object
    uses the global default Gurobi environment::

        with SolverFactory('gurobi', solver_io='python') as opt:
            opt.solve(model)

        # Only models created by `opt` are freed, the global default
        # environment remains active

    ``manage_env=True`` is required when setting license or connection parameters
    programmatically. The ``options`` argument is used to pass parameters to the
    Gurobi environment. For example, to connect to a Gurobi Cluster Manager::

        options = {
            "CSManager": "<url>",
            "CSAPIAccessID": "<access-id>",
            "CSAPISecret": "<api-key>",
        }
        with SolverFactory(
            'gurobi', solver_io='python', manage_env=True, options=options
        ) as opt:
            opt.solve(model)  # Model solved on compute server
        # Compute server connection terminated
    """
    _name = ...
    _version = ...
    _version_major = ...
    _default_env_started = ...
    def __init__(self, manage_env=..., **kwds) -> None:
        ...
    
    def available(self, exception_flag=...): # -> bool:
        """Returns True if the solver is available.

        :param exception_flag: If True, raise an exception instead of returning
            False if the solver is unavailable (defaults to False)
        :type exception_flag: bool

        In general, ``available()`` does not need to be called by the user, as
        the check is run automatically when solving a model. However it is useful
        for a simple retry loop when using a shared Gurobi license::

            with SolverFactory('gurobi', solver_io='python') as opt:
                while not available(exception_flag=False):
                    time.sleep(1)
                opt.solve(model)

        """
        ...
    
    def close_global(self): # -> None:
        """Frees all Gurobi models used by this solver, and frees the global
        default Gurobi environment.

        The default environment is used by all ``GurobiDirect`` solvers started
        with ``manage_env=False`` (the default). To guarantee that all Gurobi
        resources are freed, all instantiated ``GurobiDirect`` solvers must also
        be correctly closed.

        The following example will free all Gurobi resources assuming the user did
        not create any other models (e.g. via another ``GurobiDirect`` object with
        ``manage_env=False``)::

            opt = SolverFactory('gurobi', solver_io='python')
            try:
                opt.solve(model)
            finally:
                opt.close_global()
            # All Gurobi models created by `opt` are freed and the default
            # Gurobi environment is closed
        """
        ...
    
    def close(self): # -> None:
        """Frees local Gurobi resources used by this solver instance.

        All Gurobi models created by the solver are freed. If the solver was
        created with ``manage_env=True``, this method also closes the Gurobi
        environment used by this solver instance. Calling ``.close()`` achieves
        the same result as exiting the solver context (although using context
        managers is preferred where possible)::

            opt = SolverFactory('gurobi', solver_io='python', manage_env=True)
            try:
                opt.solve(model)
            finally:
                opt.close()
            # Gurobi models and environments created by `opt` are freed

        As with the context manager, if ``manage_env=False`` (the default) was
        used, only the Gurobi models created by this solver are freed. The
        default global Gurobi environment will still be active::

            opt = SolverFactory('gurobi', solver_io='python')
            try:
                opt.solve(model)
            finally:
                opt.close()
            # Gurobi models created by `opt` are freed; however the
            # default/global Gurobi environment is still active
        """
        ...
    
    def __exit__(self, t, v, traceback): # -> None:
        ...
    
    def warm_start_capable(self): # -> Literal[True]:
        ...
    
    def load_duals(self, cons_to_load=...): # -> None:
        """
        Load the duals into the 'dual' suffix. The 'dual' suffix must live on the parent model.

        Parameters
        ----------
        cons_to_load: list of Constraint
        """
        ...
    
    def load_rc(self, vars_to_load): # -> None:
        """
        Load the reduced costs into the 'rc' suffix. The 'rc' suffix must live on the parent model.

        Parameters
        ----------
        vars_to_load: list of Var
        """
        ...
    
    def load_slacks(self, cons_to_load=...): # -> None:
        """
        Load the values of the slack variables into the 'slack' suffix. The 'slack' suffix must live on the parent
        model.

        Parameters
        ----------
        cons_to_load: list of Constraint
        """
        ...
    

