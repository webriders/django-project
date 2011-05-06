import types
from django.utils.importlib import import_module

def get_module(module):
    '''
    get_module(str/module) -> module
    Import module if it's name was passed.
    '''
    if isinstance(module, str):
        module = import_module(module)
    return module

def get_module_constants_dict(module):
    '''
    Return module dict.
    Contains only UPPERCASE attributes that not starts with '_'.
    '''
    module = get_module(module)
    module_dict = {}
    if isinstance(module, types.ModuleType):
        for key, value in module.__dict__.iteritems():
            if key and key.isupper() and key[0] != '_':
                module_dict[key] = value
    return module_dict

def get_module_attr(module, name):
    module = get_module(module)
    return getattr(module, name)

def set_module_attr(module, name, value):
    module = get_module(module)
    setattr(module, name, value)

def update_module_list_attr(module, name, value, position='last', item=None, default_module=None):
    '''
    Updates list setting.

    position - 'first', 'last', 'before', 'after'
    item - used only with positions 'before' or 'after'
    default_module - reserved module that contains default initial value. Not required.
    '''
    list_attr = []
    try:
        list_attr = get_module_attr(module, name)
    except AttributeError:
        if default_module:
            try:
                list_attr = get_module_attr(default_module, name)
            except AttributeError:
                pass

    index = len(list_attr)
    if position == 'first':
        index = 0
    elif position == 'last':
        index = len(list_attr)
    elif position == 'before':
        index = 0
        for i, iter_item in enumerate(list_attr):
            if iter_item == item:
                index = i
                break
    elif position == 'after':
        index = len(list_attr)
        for i, iter_item in enumerate(list_attr):
            if iter_item == item:
                index = i + 1
                break
    elif isinstance(position, int):
        index = position
    else:
        raise Exception("position must be in ['first', 'last', 'before', 'after'] or int")
    list_attr.insert(index, value)
    set_module_attr(module, name, list_attr)