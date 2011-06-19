from django.utils import importlib


def get_module(module):
    """
    get_module(str/module) -> module
    Import module if string was passed.
    """
    if isinstance(module, str):
        module = importlib.import_module(module)
    return module


def get_module_consts(module):
    """
    Return dict of UPPERCASE module attributes (that doesn't starts with "_")
    """
    module = get_module(module)
    module_dict = {}
    for key in dir(module):
        if key and key.isupper() and key[0] != '_':
            module_dict[key] = getattr(module, key)
    return module_dict
