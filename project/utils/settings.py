from project.utils.modules import get_module, get_module_constants_dict, \
    get_module_attr, set_module_attr, update_module_list_attr

def import_settings(module, result):
    settings_dict = get_module_constants_dict(module)
    result.update(settings_dict)

def get_settings():
    return get_module('conf.settings')

def get_setting(name):
    return get_module_attr('conf.settings', name)

def set_setting(name, value):
    return set_module_attr('conf.settings', name, value)

def update_setting_list(name, value, **kwargs):
    kwargs['default_module'] = 'django.conf.global_settings'
    return update_module_list_attr('conf.settings', name, value, **kwargs)