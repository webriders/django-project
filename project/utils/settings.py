from project.utils.lists import merge
from project.utils.modules import get_module, get_module_consts, get_module_attr, set_module_attr


def get_settings():
    return get_module('conf.settings')


def get_setting(name):
    return get_module_attr('conf.settings', name)


def get_default_setting(name):
    return get_module_attr('django.conf.global_settings', name)


def set_setting(name, value):
    return set_module_attr('conf.settings', name, value)


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
            set_setting(key, merge(xst, option))
        else:
            set_setting(key, option)


def import_settings(globals):
    settings_dict = get_module_consts('conf.settings')
    globals.update(settings_dict)