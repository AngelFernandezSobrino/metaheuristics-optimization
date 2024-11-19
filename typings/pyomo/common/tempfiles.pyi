"""
This type stub file was generated by pyright.
"""

from pyomo.common.deprecation import deprecated

deletion_errors_are_fatal = ...
logger = ...
class TempfileManagerClass:
    """A class for managing tempfile contexts

    Pyomo declares a global instance of this class as ``TempfileManager``:

    .. doctest::

       >>> from pyomo.common.tempfiles import TempfileManager

    This class provides an interface for managing
    :class:`TempfileContext` contexts.  It implements a basic stack,
    where users can :meth:`push()` a new context (causing it to become
    the current "active" context) and :meth:`pop()` contexts off
    (optionally deleting all files associated with the context).  In
    general usage, users will either use this class to create new
    tempfile contexts and use them explicitly (i.e., through a context
    manager):

    .. doctest::

       >>> import os
       >>> with TempfileManager.new_context() as tempfile:
       ...     fd, fname = tempfile.mkstemp()
       ...     dname = tempfile.mkdtemp()
       ...     os.path.isfile(fname)
       ...     os.path.isdir(dname)
       True
       True
       >>> os.path.exists(fname)
       False
       >>> os.path.exists(dname)
       False

    or through an implicit active context accessed through the manager
    class:

    .. doctest::

       >>> TempfileManager.push()
       <pyomo.common.tempfiles.TempfileContext object ...>
       >>> fname = TempfileManager.create_tempfile()
       >>> dname = TempfileManager.create_tempdir()
       >>> os.path.isfile(fname)
       True
       >>> os.path.isdir(dname)
       True

       >>> TempfileManager.pop()
       <pyomo.common.tempfiles.TempfileContext object ...>
       >>> os.path.exists(fname)
       False
       >>> os.path.exists(dname)
       False

    """
    def __init__(self) -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def shutdown(self, remove=...): # -> None:
        ...
    
    def context(self):
        """Return the current active TempfileContext.

        Raises
        ------
        TempfileContextError if there is not a current context."""
        ...
    
    def create_tempfile(self, suffix=..., prefix=..., text=..., dir=...):
        "Call :meth:`TempfileContext.create_tempfile` on the active context"
        ...
    
    def create_tempdir(self, suffix=..., prefix=..., dir=...):
        "Call :meth:`TempfileContext.create_tempdir` on the active context"
        ...
    
    def add_tempfile(self, filename, exists=...):
        "Call :meth:`TempfileContext.add_tempfile` on the active context"
        ...
    
    def clear_tempfiles(self, remove=...): # -> None:
        """Delete all temporary files and remove all contexts."""
        ...
    
    @deprecated("The TempfileManager.sequential_files() method has been " "removed.  All temporary files are created with guaranteed " "unique names.  Users wishing sequentially numbered files " "should create a temporary (empty) directory using mkdtemp " "/ create_tempdir and place the sequential files within it.", version='6.2')
    def sequential_files(self, ctr=...): # -> None:
        ...
    
    def unique_files(self): # -> None:
        ...
    
    def new_context(self): # -> TempfileContext:
        """Create and return an new tempfile context

        Returns
        -------
        TempfileContext
            the newly-created tempfile context

        """
        ...
    
    def push(self): # -> TempfileContext:
        """Create a new tempfile context and set it as the active context.

        Returns
        -------
        TempfileContext
            the newly-created tempfile context

        """
        ...
    
    def pop(self, remove=...):
        """Remove and release the active context

        Parameters
        ----------
        remove: bool
            If ``True``, delete all managed files / directories

        """
        ...
    
    def __enter__(self): # -> TempfileContext:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb): # -> None:
        ...
    


class TempfileContext:
    """A `context` for managing collections of temporary files

    Instances of this class hold a "temporary file context".  That is,
    this records a collection of temporary file system objects that are
    all managed as a group.  The most common use of the context is to
    ensure that all files are deleted when the context is released.

    This class replicates a significant portion of the :mod:`tempfile`
    module interface.

    Instances of this class may be used as context managers (with the
    temporary files / directories getting automatically deleted when the
    context manager exits).

    Instances will also attempt to delete any temporary objects from the
    filesystem when the context falls out of scope (although this
    behavior is not guaranteed for instances existing when the
    interpreter is shutting down).

    """
    def __init__(self, manager) -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb): # -> None:
        ...
    
    def mkstemp(self, suffix=..., prefix=..., dir=..., text=...): # -> tuple[int, str]:
        """Create a unique temporary file using :func:`tempfile.mkstemp`

        Parameters are handled as in :func:`tempfile.mkstemp`, with
        the exception that the new file is created in the directory
        returned by :meth:`gettempdir`

        Returns
        -------
        fd: int
            the opened file descriptor

        fname: str or bytes
            the absolute path to the new temporary file

        """
        ...
    
    def mkdtemp(self, suffix=..., prefix=..., dir=...): # -> str:
        """Create a unique temporary directory using :func:`tempfile.mkdtemp`

        Parameters are handled as in :func:`tempfile.mkdtemp`, with
        the exception that the new file is created in the directory
        returned by :meth:`gettempdir`

        Returns
        -------
        dname: str or bytes
            the absolute path to the new temporary directory

        """
        ...
    
    def gettempdir(self): # -> str | Any:
        """Return the default name of the directory used for temporary files.

        This method returns the first non-null location returned from:

         - This context's ``tempdir`` (i.e., ``self.tempdir``)
         - This context's manager's ``tempdir`` (i.e.,
           ``self.manager().tempdir``)
         - :func:`tempfile.gettempdir()`

        Returns
        -------
        dir: str
            The default directory to use for creating temporary objects
        """
        ...
    
    def gettempdirb(self): # -> bytes | Any:
        """Same as :meth:`gettempdir()`, but the return value is ``bytes``"""
        ...
    
    def gettempprefix(self): # -> str:
        """Return the filename prefix used to create temporary files.

        See :func:`tempfile.gettempprefix()`

        """
        ...
    
    def gettempprefixb(self): # -> bytes:
        """Same as :meth:`gettempprefix()`, but the return value is ``bytes``"""
        ...
    
    def create_tempfile(self, suffix=..., prefix=..., text=..., dir=...): # -> str:
        """Create a unique temporary file.

        The file name is generated as in :func:`tempfile.mkstemp()`.

        Any file handles to the new file (e.g., from :meth:`mkstemp`)
        are closed.

        Returns
        -------
        fname: str or bytes
            The absolute path of the new file.

        """
        ...
    
    def create_tempdir(self, suffix=..., prefix=..., dir=...): # -> str:
        """Create a unique temporary directory.

        The file name is generated as in :func:`tempfile.mkdtemp()`.

        Returns
        -------
        dname: str or bytes
            The absolute path of the new directory.

        """
        ...
    
    def add_tempfile(self, filename, exists=...): # -> None:
        """Declare the specified file/directory to be temporary.

        This adds the specified path as a "temporary" object to this
        context's list of managed temporary paths (i.e., it will be
        potentially be deleted when the context is released (see
        :meth:`release`).

        Parameters
        ----------
        filename: str
            the file / directory name to be treated as temporary
        exists: bool
            if ``True``, the file / directory must already exist.

        """
        ...
    
    def release(self, remove=...): # -> None:
        """Release this context

        This releases the current context, potentially deleting all
        managed temporary objects (files and directories), and resetting
        the context to generate unique names.

        Parameters
        ----------
        remove: bool
            If ``True``, delete all managed files / directories
        """
        ...
    


TempfileManager: TempfileManagerClass = ...