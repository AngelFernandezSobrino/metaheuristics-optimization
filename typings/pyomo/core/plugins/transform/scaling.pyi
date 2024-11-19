"""
This type stub file was generated by pyright.
"""

from pyomo.core.base import TransformationFactory
from pyomo.core.plugins.transform.hierarchy import Transformation

logger = ...
@TransformationFactory.register('core.scale_model', doc="Scale model variables, constraints, and objectives.")
class ScaleModel(Transformation):
    """
    Transformation to scale a model.

    This plugin performs variable, constraint, and objective scaling on
    a model based on the scaling factors in the suffix 'scaling_factor'
    set for the variables, constraints, and/or objective. This is typically
    done to scale the problem for improved numerical properties.

    Supported transformation methods:
        * :py:meth:`apply_to <pyomo.core.plugins.transform.scaling.ScaleModel.apply_to>`
        * :py:meth:`create_using <pyomo.core.plugins.transform.scaling.ScaleModel.create_using>`
        * :py:meth:`propagate_solution <pyomo.core.plugins.transform.scaling.ScaleModel.propagate_solution>`

    By default, scaling components are renamed with the prefix ``scaled_``. To disable
    this behavior and scale variables in-place (or keep the same names in a new model),
    use the ``rename=False`` argument to ``apply_to`` or ``create_using``.


    Examples
    --------

    .. doctest::

        >>> from pyomo.environ import *
        >>> # create the model
        >>> model = ConcreteModel()
        >>> model.x = Var(bounds=(-5, 5), initialize=1.0)
        >>> model.y = Var(bounds=(0, 1), initialize=1.0)
        >>> model.obj = Objective(expr=1e8*model.x + 1e6*model.y)
        >>> model.con = Constraint(expr=model.x + model.y == 1.0)
        >>> # create the scaling factors
        >>> model.scaling_factor = Suffix(direction=Suffix.EXPORT)
        >>> model.scaling_factor[model.obj] = 1e-6 # scale the objective
        >>> model.scaling_factor[model.con] = 2.0  # scale the constraint
        >>> model.scaling_factor[model.x] = 0.2    # scale the x variable
        >>> # transform the model
        >>> scaled_model = TransformationFactory('core.scale_model').create_using(model)
        >>> # print the value of the objective function to show scaling has occurred
        >>> print(value(model.x))
        1.0
        >>> print(value(scaled_model.scaled_x))
        0.2
        >>> print(value(scaled_model.scaled_x.lb))
        -1.0
        >>> print(value(model.obj))
        101000000.0
        >>> print(value(scaled_model.scaled_obj))
        101.0

    """
    def __init__(self, **kwds) -> None:
        ...
    
    def propagate_solution(self, scaled_model, original_model): # -> None:
        """This method takes the solution in scaled_model and maps it back to
        the original model.

        It will also transform duals and reduced costs if the suffixes
        'dual' and/or 'rc' are present.  The :code:`scaled_model`
        argument must be a model that was already scaled using this
        transformation as it expects data from the transformation to
        perform the back mapping.

        Parameters
        ----------
        scaled_model : Pyomo Model
           The model that was previously scaled with this transformation
        original_model : Pyomo Model
           The original unscaled source model

        """
        ...
    

