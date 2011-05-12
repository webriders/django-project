from django.utils.importlib import import_module


def get_module(module):
    '''
    get_module(str/module) -> module
    Import module if string was passed.
    '''
    if isinstance(module, str):
        module = import_module(module)
    return module


def get_module_attr(module, name):
    module = get_module(module)
    return getattr(module, name)


def set_module_attr(module, name, value):
    module = get_module(module)
    setattr(module, name, value)


def get_module_constants_dict(module):
    '''
    Return dict of UPPERCASE module attributes (that alse not starts with '_')
    '''
    module = get_module(module)
    module_dict = {}
    for key in dir(module):
        if key and key.isupper() and key[0] != '_':
            module_dict[key] = getattr(module, key)
    return module_dict
