"""
This type stub file was generated by pyright.
"""

from pyomo.common.errors import PyomoException
from pyomo.common.deprecation import deprecated

class PluginGlobals:
    @staticmethod
    @deprecated("The PluginGlobals environment manager is deprecated: " "Pyomo only supports a single global environment", version='6.0')
    def add_env(name): # -> None:
        ...
    
    @staticmethod
    @deprecated("The PluginGlobals environment manager is deprecated: " "Pyomo only supports a single global environment", version='6.0')
    def pop_env(): # -> None:
        ...
    
    @staticmethod
    @deprecated("The PluginGlobals environment manager is deprecated: " "Pyomo only supports a single global environment", version='6.0')
    def clear(): # -> None:
        ...
    


class PluginError(PyomoException):
    ...


def alias(name, doc=..., subclass=...): # -> None:
    ...

def implements(interface, inherit=..., namespace=..., service=...): # -> None:
    ...

class InterfaceMeta(type):
    def __new__(cls, name, bases, classdict, *args, **kwargs): # -> Self:
        ...
    


class Interface(metaclass=InterfaceMeta):
    ...


class _deprecated_plugin_dict(dict):
    def __init__(self, name, classdict) -> None:
        ...
    
    def __setitem__(self, key, val): # -> None:
        ...
    
    def items(self): # -> dict_items[Any, Any]:
        ...
    


class DeprecatedInterfaceMeta(InterfaceMeta):
    def __new__(cls, name, bases, classdict, *args, **kwargs): # -> Self:
        ...
    


class DeprecatedInterface(Interface, metaclass=DeprecatedInterfaceMeta):
    ...


class PluginMeta(type):
    def __new__(cls, name, bases, classdict, *args, **kwargs): # -> Self | tmp_meta:
        ...
    


class Plugin(metaclass=PluginMeta):
    def __new__(cls): # -> Self:
        ...
    
    def activate(self): # -> None:
        ...
    
    enable = ...
    def deactivate(self): # -> None:
        ...
    
    disable = ...
    def enabled(self): # -> bool:
        ...
    


class SingletonPlugin(Plugin):
    __singleton__ = ...


class ExtensionPoint:
    def __init__(self, interface) -> None:
        ...
    
    def __iter__(self, key=..., all=...): # -> Generator[Any, Any, None]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def extensions(self, all=..., key=...): # -> list[Any]:
        ...
    
    def __call__(self, key=..., all=...): # -> list[Any]:
        ...
    
    def service(self, key=..., all=...): # -> None:
        """Return the unique service that matches the interface of this
        extension point.  An exception occurs if no service matches the
        specified key, or if multiple services match.
        """
        ...
    


class PluginFactory:
    def __init__(self, interface) -> None:
        ...
    
    def __call__(self, name, *args, **kwds): # -> None:
        ...
    
    def services(self): # -> list[Any]:
        ...
    
    def get_class(self, name):
        ...
    
    def doc(self, name): # -> Literal['']:
        ...
    
    def deactivate(self, name): # -> None:
        ...
    
    def activate(self, name): # -> None:
        ...
    


CreatePluginFactory = PluginFactory
