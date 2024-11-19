"""
This type stub file was generated by pyright.
"""

class PiecewiseValidationError(Exception):
    """An exception raised when validation of piecewise
    linear functions fail."""
    ...


def is_constant(vals): # -> bool:
    """Checks if a list of points is constant"""
    ...

def is_nondecreasing(vals): # -> bool:
    """Checks if a list of points is nondecreasing"""
    ...

def is_nonincreasing(vals): # -> bool:
    """Checks if a list of points is nonincreasing"""
    ...

def is_positive_power_of_two(x): # -> Literal[False]:
    """Checks if a number is a nonzero and positive power of 2"""
    ...

def log2floor(n):
    """Computes the exact value of floor(log2(n)) without
    using floating point calculations. Input argument must
    be a positive integer."""
    ...

def generate_gray_code(nbits): # -> list[list[int]]:
    """Generates a Gray code of nbits as list of lists"""
    ...

def characterize_function(breakpoints, values): # -> tuple[Any, list[Any]]:
    """
    Characterizes a piecewise linear function described by a
    list of breakpoints and function values.

    Args:
        breakpoints (list): The list of breakpoints of the
            piecewise linear function. It is assumed that
            the list of breakpoints is in non-decreasing
            order.
        values (list): The values of the piecewise linear
            function corresponding to the breakpoints.

    Returns:
        (int, list): a function characterization code and
            the list of slopes.

    .. note::
        The function characterization codes are

          * 1: affine
          * 2: convex
          * 3: concave
          * 4: step
          * 5: other

        If the function has step points, some of the slopes
        may be :const:`None`.
    """
    ...

def generate_delaunay(variables, num=..., **kwds): # -> Any:
    """
    Generate a Delaunay triangulation of the D-dimensional
    bounded variable domain given a list of D variables.

    Requires numpy and scipy.

    Args:
        variables: A list of variables, each having a finite
            upper and lower bound.
        num (int): The number of grid points to generate for
            each variable (default=10).
        **kwds: All additional keywords are passed to the
          scipy.spatial.Delaunay constructor.

    Returns:
        A scipy.spatial.Delaunay object.
    """
    ...
