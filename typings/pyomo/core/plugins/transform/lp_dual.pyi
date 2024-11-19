"""
This type stub file was generated by pyright.
"""

from pyomo.common.autoslots import AutoSlots
from pyomo.core import TransformationFactory

class _LPDualData(AutoSlots.Mixin):
    __slots__ = ...
    def __init__(self) -> None:
        ...
    


@TransformationFactory.register('core.lp_dual', 'Generate the linear programming dual of the given model')
class LinearProgrammingDual:
    CONFIG = ...
    def apply_to(self, model, **options):
        ...
    
    def create_using(self, model, ostream=..., **kwds): # -> ConcreteModel:
        """Take linear programming dual of a model

        Returns
        -------
        ConcreteModel containing linear programming dual

        Parameters
        ----------
        model: ConcreteModel
            The concrete Pyomo model to take the dual of

        ostream: None
            This is provided for API compatibility with other writers
            and is ignored here.

        """
        ...
    
    def get_primal_constraint(self, model, dual_var):
        """Return the primal constraint corresponding to 'dual_var'

        Returns
        -------
        Constraint

        Parameters
        ----------
        model: ConcreteModel
            A dual model returned from the 'core.lp_dual' transformation
        dual_var: Var
            A dual variable on 'model'

        """
        ...
    
    def get_dual_constraint(self, model, primal_var):
        """Return the dual constraint corresponding to 'primal_var'

        Returns
        -------
        Constraint

        Parameters
        ----------
        model: ConcreteModel
            A primal model passed as an argument to the 'core.lp_dual' transformation
        primal_var: Var
            A primal variable on 'model'

        """
        ...
    
    def get_primal_var(self, model, dual_constraint):
        """Return the primal variable corresponding to 'dual_constraint'

        Returns
        -------
        Var

        Parameters
        ----------
        model: ConcreteModel
            A dual model returned from the 'core.lp_dual' transformation
        dual_constraint: Constraint
            A constraint on 'model'

        """
        ...
    
    def get_dual_var(self, model, primal_constraint):
        """Return the dual variable corresponding to 'primal_constraint'

        Returns
        -------
        Var

        Parameters
        ----------
        model: ConcreteModel
            A primal model passed as an argument to the 'core.lp_dual' transformation
        primal_constraint: Constraint
            A constraint on 'model'

        """
        ...
    


