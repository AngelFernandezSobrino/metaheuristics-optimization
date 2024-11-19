"""
This type stub file was generated by pyright.
"""

from pyomo.core.base import Transformation, TransformationFactory

logger = ...
@TransformationFactory.register("core.radix_linearization", doc="Linearize bilinear and quadratic terms through " "radix discretization (multiparametric disaggregation)")
class RadixLinearization(Transformation):
    """
    This plugin generates linear relaxations of bilinear problems using
    the multiparametric disaggregation technique of Kolodziej, Castro,
    and Grossmann.  See:

    Scott Kolodziej, Pedro M. Castro, and Ignacio E. Grossmann. "Global
       optimization of bilinear programs with a multiparametric
       disaggregation technique."  J.Glob.Optim 57 pp.1039-1063. 2013.
       (DOI 10.1007/s10898-012-0022-1)
    """
    ...


