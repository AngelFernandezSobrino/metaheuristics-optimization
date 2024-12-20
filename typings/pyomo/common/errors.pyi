"""
This type stub file was generated by pyright.
"""

def format_exception(msg, prolog=..., epilog=..., exception=..., width=...): # -> LiteralString:
    """Generate a formatted exception message

    This returns a formatted exception message, line wrapped for display
    on the console and with optional prolog and epilog messages.

    Parameters
    ----------
    msg: str
        The raw exception message

    prolog: str, optional
        A message to output before the exception message, ``msg``.  If
        this message is long enough to line wrap, the ``msg`` will be
        indented a level below the ``prolog`` message.

    epilog: str, optional
        A message to output after the exception message, ``msg``.  If
        provided, the ``msg`` will be indented a level below the
        ``prolog`` / ``epilog`` messages.

    exception: Exception, optional
        The raw exception being raised (used to improve initial line wrapping).

    width: int, optional
        The line length to wrap the exception message to.

    Returns
    -------
    str
    """
    ...

class ApplicationError(Exception):
    """
    An exception used when an external application generates an error.
    """
    ...


class PyomoException(Exception):
    """
    Exception class for other Pyomo exceptions to inherit from,
    allowing Pyomo exceptions to be caught in a general way
    (e.g., in other applications that use Pyomo).
    """
    ...


class DeferredImportError(ImportError):
    """This exception is raised when something attempts to access a module
    that was imported by :py:func:`.attempt_import`, but the module
    import failed.

    """
    ...


class DeveloperError(PyomoException, NotImplementedError):
    """
    Exception class used to throw errors that result from Pyomo
    programming errors, rather than user modeling errors (e.g., a
    component not declaring a 'ctype').
    """
    def __str__(self) -> str:
        ...
    


class InfeasibleConstraintException(PyomoException):
    """
    Exception class used by Pyomo transformations to indicate
    that an infeasible constraint has been identified (e.g. in
    the course of range reduction).
    """
    ...


class IterationLimitError(PyomoException, RuntimeError):
    """A subclass of :py:class:`RuntimeError`, raised by an iterative method
    when the iteration limit is reached.

    TODO: solvers currently do not raise this exception, but probably
    should (at least when non-normal termination conditions are mapped
    to exceptions)

    """
    ...


class IntervalException(PyomoException, ValueError):
    """
    Exception class used for errors in interval arithmetic.
    """
    ...


class InvalidValueError(PyomoException, ValueError):
    """
    Exception class used for value errors in compiled model representations
    """
    ...


class MouseTrap(PyomoException, NotImplementedError):
    """
    Exception class used to throw errors for not-implemented functionality
    that might be rational to support (i.e., we already gave you a cookie)
    but risks taking Pyomo's flexibility a step beyond what is sane,
    or solvable, or communicable to a solver, etc. (i.e., Really? Now you
    want a glass of milk too?)
    """
    def __str__(self) -> str:
        ...
    


class NondifferentiableError(PyomoException, ValueError):
    """A Pyomo-specific ValueError raised for non-differentiable expressions"""
    ...


class TempfileContextError(PyomoException, IndexError):
    """A Pyomo-specific IndexError raised when attempting to use the
    TempfileManager when it does not have a currently active context.

    """
    ...


class TemplateExpressionError(ValueError):
    """Special ValueError raised by getitem for template arguments

    This exception is triggered by the Pyomo expression system when
    attempting to get a member of an IndexedComponent using either a
    TemplateIndex, or an expression containing a TemplateIndex.

    Users should never see this exception.

    """
    def __init__(self, template, *args, **kwds) -> None:
        ...
    


