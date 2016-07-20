import sys
from types import ModuleType
from types import FunctionType


def modules_in_module(module):
    md = module.__dict__
    return [
        md[c] for c in md if (
            isinstance(md[c], ModuleType)
        )
    ]

def classes_in_module(module):
    md = module.__dict__
    return [
        md[c] for c in md if (
            isinstance(md[c], type)
        )
    ]


def functions_in_class(module):
    md = module.__dict__
    return [
        md[c] for c in md if (
            isinstance(md[c], FunctionType)
        )
    ]

def add_func_to_module(module, func):
    setattr(module, func.__name__, func)

def copy_functions_to_module(module):
    classList = classes_in_module(module)
    for c in classList:
        for f in functions_in_class(c):
            add_func_to_module(module, f)

    modules = modules_in_module(module)
    for m in modules:
        copy_functions_to_module(m)

