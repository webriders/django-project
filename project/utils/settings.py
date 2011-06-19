from django.conf import BaseSettings, global_settings


class SettingsStorage(BaseSettings):
    def __init__(self):
        for setting in dir(global_settings):
            if setting == setting.upper():
                setattr(self, setting, getattr(global_settings, setting))

    def to_dict(self):
        res = {}
        for setting in dir(self):
            if setting == setting.upper():
                res[setting] = getattr(self, setting)
        return res

settings_storage = SettingsStorage()


def get_settings():
    return settings_storage


def import_settings(globals):
    globals.update(settings_storage.to_dict())


def get_setting(name, default=None):
    return getattr(settings_storage, name, default)


def set_setting(name, value):
    return setattr(settings_storage, name, value)


def get_list_setting(name):
    setting = get_setting(name, [])
    if not isinstance(setting, (list, tuple)):
        raise Exception(u"Setting should be a list or tuple but it's not: %s == %s" % (name, unicode(setting)))
    return list(setting)


def append_setting(name, value):
    setting = get_list_setting(name)
    if not isinstance(value, (list, tuple)):
        value = [value]
    value = list(value)
    for i in value:
        if i not in setting:
            setting.append(i)
    set_setting(name, setting)


def prepend_setting(name, value):
    setting = get_list_setting(name)
    if not isinstance(value, (list, tuple)):
        value = [value]
    value = list(value)
    value.reverse()
    for i in value:
        if i not in setting:
            setting.insert(0, i)
    set_setting(name, setting)
