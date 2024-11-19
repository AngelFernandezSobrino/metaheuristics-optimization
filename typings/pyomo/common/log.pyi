"""
This type stub file was generated by pyright.
"""

import io
import logging
from pyomo.common.deprecation import deprecated

_indentation_re = ...
_RTD_URL = ...
def RTD(_id): # -> str:
    ...

_DEBUG = ...
_NOTSET = ...
if not __debug__:
    def is_debug_set(logger): # -> Literal[False]:
        ...
    
else:
    def is_debug_set(logger): # -> Literal[False]:
        """A variant of Logger.isEnableFor that returns False if NOTSET

        The implementation of logging.Logger.isEnableFor() returns True
        if the effective level of the logger is NOTSET.  This variant
        only returns True if the effective level of the logger is NOTSET
        < level <= DEBUG.  This is used in Pyomo to detect if the user
        explicitly requested DEBUG output.

        This implementation mimics the core functionality of
        isEnabledFor() by directly querying the (undocumented) 'manager'
        attribute to get the current value for logging.disabled()

        """
        ...
    
    def is_debug_set(logger): # -> Literal[False]:
        ...
    
class WrappingFormatter(logging.Formatter):
    _flag = ...
    def __init__(self, **kwds) -> None:
        ...
    
    def format(self, record): # -> str:
        ...
    


class LegacyPyomoFormatter(logging.Formatter):
    """This mocks up the legacy Pyomo log formatting.

    This formatter takes a callback function (`verbosity`) that will be
    called for each message.  Based on the result, one of two formatting
    templates will be used.

    """
    def __init__(self, **kwds) -> None:
        ...
    
    def format(self, record): # -> str:
        ...
    


class StdoutHandler(logging.StreamHandler):
    """A logging handler that emits to the current value of sys.stdout"""
    def flush(self): # -> None:
        ...
    
    def emit(self, record): # -> None:
        ...
    


class Preformatted:
    __slots__ = ...
    def __init__(self, msg) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class _GlobalLogFilter:
    def __init__(self) -> None:
        ...
    
    def filter(self, record): # -> bool:
        ...
    


pyomo_logger = ...
pyomo_handler = ...
pyomo_formatter = ...
@deprecated('The pyomo.common.log.LogHandler class has been deprecated ' 'in favor of standard Handlers from the Python logging module ' 'combined with the pyomo.common.log.WrappingFormatter.', version='5.7.3')
class LogHandler(logging.StreamHandler):
    def __init__(self, base=..., stream=..., level=..., verbosity=...) -> None:
        ...
    


class LoggingIntercept:
    r"""Context manager for intercepting messages sent to a log stream

    This class is designed to enable easy testing of log messages.

    The LoggingIntercept context manager will intercept messages sent to
    a log stream matching a specified level and send the messages to the
    specified output stream.  Other handlers registered to the target
    logger will be temporarily removed and the logger will be set not to
    propagate messages up to higher-level loggers.

    Parameters
    ----------
    output: io.TextIOBase
        the file stream to send log messages to
    module: str
        the target logger name to intercept
    level: int
        the logging level to intercept
    formatter: logging.Formatter
        the formatter to use when rendering the log messages.  If not
        specified, uses `'%(message)s'`

    Examples
    --------
    >>> import io, logging
    >>> from pyomo.common.log import LoggingIntercept
    >>> buf = io.StringIO()
    >>> with LoggingIntercept(buf, 'pyomo.core', logging.WARNING):
    ...     logging.getLogger('pyomo.core').warning('a simple message')
    >>> buf.getvalue()
    'a simple message\n'

    """
    def __init__(self, output=..., module=..., level=..., formatter=...) -> None:
        ...
    
    def __enter__(self): # -> StringIO:
        ...
    
    def __exit__(self, et, ev, tb): # -> None:
        ...
    


class LogStream(io.TextIOBase):
    """
    This class logs whatever gets sent to the write method.
    This is useful for logging solver output (a LogStream
    instance can be handed to TeeStream from pyomo.common.tee).
    """
    def __init__(self, level, logger) -> None:
        ...
    
    def write(self, s: str) -> int:
        ...
    
    def flush(self): # -> None:
        ...
    


