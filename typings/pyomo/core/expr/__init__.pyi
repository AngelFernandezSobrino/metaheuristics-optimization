"""
This type stub file was generated by pyright.
"""

from . import boolean_value, logical_expr, numeric_expr, numvalue, relational_expr, visitor
from pyomo.common.numeric_types import native_numeric_types, native_types, nonpyomo_leaf_types, value
from pyomo.common.errors import TemplateExpressionError
from .base import ExpressionBase
from .boolean_value import BooleanValue
from .expr_common import ExpressionType, Mode, OperatorAssociativity
from .logical_expr import AllDifferentExpression, AndExpression, AtLeastExpression, AtMostExpression, BinaryBooleanExpression, BooleanConstant, BooleanExpression, BooleanExpressionBase, BooleanValue, CountIfExpression, EquivalenceExpression, ExactlyExpression, ImplicationExpression, NaryBooleanExpression, NotExpression, OrExpression, UnaryBooleanExpression, XorExpression, all_different, atleast, atmost, count_if, equivalent, exactly, implies, land, lnot, lor, native_logical_types, special_boolean_atom_types, xor
from .numeric_expr import AbsExpression, DivisionExpression, Expr_if, Expr_ifExpression, ExternalFunctionExpression, LinearDecompositionError, LinearExpression, MaxExpression, MinExpression, MonomialTermExpression, NPV_AbsExpression, NPV_DivisionExpression, NPV_Expr_ifExpression, NPV_ExternalFunctionExpression, NPV_MaxExpression, NPV_MinExpression, NPV_NegationExpression, NPV_PowExpression, NPV_ProductExpression, NPV_SumExpression, NPV_UnaryFunctionExpression, NPV_expression_types, NegationExpression, NumericExpression, NumericValue, PowExpression, ProductExpression, SumExpression, SumExpressionBase, UnaryFunctionExpression, acos, acosh, asin, asinh, atan, atanh, ceil, cos, cosh, decompose_term, exp, floor, linear_expression, log, log10, mutable_expression, nonlinear_expression, sin, sinh, sqrt, tan, tanh
from .numvalue import ZeroConstant, as_numeric, is_constant, is_fixed, is_potentially_variable, is_variable_type, polynomial_degree
from .relational_expr import EqualityExpression, InequalityExpression, NotEqualExpression, RangedExpression, RelationalExpression, inequality
from .symbol_map import SymbolMap
from .template_expr import Boolean_GetAttrExpression, Boolean_GetItemExpression, CallExpression, GetAttrExpression, GetItemExpression, IndexTemplate, NPV_Boolean_GetAttrExpression, NPV_Boolean_GetItemExpression, NPV_Numeric_GetAttrExpression, NPV_Numeric_GetItemExpression, NPV_Structural_GetAttrExpression, NPV_Structural_GetItemExpression, Numeric_GetAttrExpression, Numeric_GetItemExpression, ReplaceTemplateExpression, Structural_GetAttrExpression, Structural_GetItemExpression, TemplateSumExpression, resolve_template, substitute_getitem_with_param, substitute_template_expression, substitute_template_with_value, templatize_constraint, templatize_rule
from .visitor import ExpressionReplacementVisitor, ExpressionValueVisitor, FixedExpressionError, NonConstantExpressionError, SimpleExpressionVisitor, StreamBasedExpressionVisitor, clone_expression, evaluate_expression, expression_to_string, identify_components, identify_mutable_parameters, identify_variables, polynomial_degree, replace_expressions, sizeof_expression
from .calculus.derivatives import differentiate
from .taylor_series import taylor_series_expansion
from pyomo.common.deprecation import moved_module

