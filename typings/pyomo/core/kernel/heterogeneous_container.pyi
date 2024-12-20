"""
This type stub file was generated by pyright.
"""

from pyomo.core.kernel.base import ICategorizedObjectContainer

def heterogeneous_containers(node, ctype=..., active=..., descend_into=...): # -> Generator[Any, Any, None]:
    """
    A generator that yields all heterogeneous containers
    included in an object storage tree, including the root
    object. Heterogeneous containers are categorized objects
    with a category type different from their children.

    Args:
        node: The root object.
        ctype: Indicates the category of objects to
            include. The default value indicates that
            all categories should be included.
        active (:const:`True`/:const:`None`): Controls
            whether or not to filter the iteration to
            include only the active part of the storage
            tree. The default is :const:`True`. Setting this
            keyword to :const:`None` causes the active
            status of objects to be ignored.
        descend_into (bool, function): Indicates whether or
            not to descend into a heterogeneous
            container. Default is True, which is equivalent
            to `lambda x: True`, meaning all heterogeneous
            containers will be descended into.

    Returns:
        iterator of heterogeneous containers in the storage
        tree, include the root object.
    """
    ...

class IHeterogeneousContainer(ICategorizedObjectContainer):
    """
    A partial implementation of the ICategorizedObjectContainer
    interface for implementations that store multiple
    categories of objects.

    Complete implementations need to set the _ctype
    attribute and declare the remaining required abstract
    properties of the ICategorizedObjectContainer base
    class.
    """
    __slots__ = ...
    _is_heterogeneous_container = ...
    def collect_ctypes(self, active=..., descend_into=...): # -> set[Any]:
        """Returns the set of object category types that can
        be found under this container.

        Args:
            active (:const:`True`/:const:`None`): Controls
                whether or not to filter the iteration to
                include only the active part of the storage
                tree. The default is :const:`True`. Setting
                this keyword to :const:`None` causes the
                active status of objects to be ignored.
            descend_into (bool, function): Indicates whether
                or not to descend into a heterogeneous
                container. Default is True, which is
                equivalent to `lambda x: True`, meaning all
                heterogeneous containers will be descended
                into.

        Returns:
            A set of object category types
        """
        ...
    
    def child_ctypes(self, *args, **kwds):
        """Returns the set of child object category types
        stored in this container."""
        ...
    
    def components(self, ctype=..., active=..., descend_into=...): # -> Generator[Any, Any, None]:
        """
        Generates an efficient traversal of all components
        stored under this container. Components are
        categorized objects that are either (1) not
        containers, or (2) are heterogeneous containers.

        Args:
            ctype: Indicates the category of components to
                include. The default value indicates that
                all categories should be included.
            active (:const:`True`/:const:`None`): Controls
                whether or not to filter the iteration to
                include only the active part of the storage
                tree. The default is :const:`True`. Setting
                this keyword to :const:`None` causes the
                active status of objects to be ignored.
            descend_into (bool, function): Indicates whether
                or not to descend into a heterogeneous
                container. Default is True, which is
                equivalent to `lambda x: True`, meaning all
                heterogeneous containers will be descended
                into.

        Returns:
            iterator of components in the storage tree
        """
        ...
    


