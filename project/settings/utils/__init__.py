from project.settings.utils.modules import get_module, get_module_constants_dict, get_module_attr, set_module_attr


def import_settings(module, globals):
    settings_dict = get_module_constants_dict(module)
    globals.update(settings_dict)


def get_settings():
    return get_module('conf.settings')


def get_option(name):
    return get_module_attr('conf.settings', name)


def get_default_option(name):
    return get_module_attr('django.conf.global_settings', name)


def set_option(name, value):
    return set_module_attr('conf.settings', name, value)
