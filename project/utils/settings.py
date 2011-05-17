from project.utils.lists import merge_lists
from project.utils.modules import get_module, get_module_consts, get_module_attr, set_module_attr


SETTINGS_STORAGE = 'conf.settings.storage'
DEFAULT_SETTINGS = 'django.conf.global_settings'


def get_settings():
    return get_module(SETTINGS_STORAGE)


def get_setting(name):
    return get_module_attr(SETTINGS_STORAGE, name)


def get_default_setting(name):
    return get_module_attr(DEFAULT_SETTINGS, name)


def set_setting(name, value):
    return set_module_attr(SETTINGS_STORAGE, name, value)


def install_settings(module):
    incoming = get_module_consts(module)
    for key, option in incoming.iteritems():
        if isinstance(option, (list, tuple)):
            try:
                xst = get_setting(key)
            except AttributeError:
                try:
                    xst = get_default_setting(key)
                except AttributeError:
                    xst = []
            set_setting(key, merge_lists(xst, option))
        else:
            set_setting(key, option)


def import_settings(globals, module=SETTINGS_STORAGE):
    settings_dict = get_module_consts(module)
    globals.update(settings_dict)