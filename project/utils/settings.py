import sys
import os
from django.utils.encoding import smart_str
from django.conf import settings
from project.utils.lists import merge_lists, ListFragment, OrderedItem
from project.utils.modules import get_module_consts, get_module


def get_settings():
    return settings


def get_setting(name):
    return getattr(settings, name)


def set_setting(name, value):
    return setattr(settings, name, value)


def install_settings(settings_module):
    '''
    Install settings from the specified module.

    Conventions:
        * Only UPPERCASE settings (that doesn't starts with "_") will be installed.
        * If you've used list_fragment() - it will be merged with existent list/tuple setting
        * If you've used ordered_item() - it will be sorted according to provided before/after rules (of ALL list items)
    '''

    incoming = get_module_consts(settings_module)

    for key, option in incoming.iteritems():
        if isinstance(option, ListFragment):
            try:
                xst = get_setting(key)
            except AttributeError:
                xst = []
            set_setting(key, merge_lists(xst, option))
        else:
            set_setting(key, option)


def install_main_settings():
    '''
    Shortcut for the:
        install_settings('conf.settings.main')
    '''
    return install_settings('conf.settings.main')


def install_app_settings(app_module):
    '''
    Install django application settings.

    Settings may be presented as:
        * Python module (regular *.py file)
        * Python package (that should contain settings.py inside)

    Conventions:
        * If there is setting named "ignore" and it's bool(ignore) == True, then installation will be cancelled.
        * If there is no INSTALLED_APPS setting defined: module/package name will be used instead.
          And you may specify as many INSTALLED_APPS as you want.
    See more conventions in the "install_settings" docs - help(install_settings).
    '''
    sys.stdout.write(smart_str('Installing "%s" settings...\n' % app_module))

    try:
        app = get_module(app_module)
    except ImportError:
        sys.stderr.write(smart_str('Error: can\'t import "%s" module.' % app_module))
        sys.exit(1)

    if '__init__.py' in app.__file__:
        try:
            app_settings = get_module('.'.join([app_module, 'settings']))
        except ImportError:
            sys.stderr.write(smart_str('Error: no "settings.py" found inside "%s" package!' % app_module))
            sys.exit(1)
    else:
        app_settings = app

    if getattr(app, 'ignore', False):
        sys.stdout.write(smart_str('... "%s" settings installation ignored.\n' % app_module))
    else:
        install_settings(app_settings)

        if not hasattr(app_settings, 'INSTALLED_APPS'):
            app_name = app_module.split('.')[-1]
            INSTALLED_APPS = get_setting('INSTALLED_APPS')
            INSTALLED_APPS = merge_lists(INSTALLED_APPS, [app_name])
            set_setting('INSTALLED_APPS', INSTALLED_APPS)


def install_apps_settings(apps_package='conf.apps'):
    '''
    Installs all applications settings from the specified python package.

    See help(install_app_settings) and help(install_settings) for more info.
    '''
    apps_folder = get_module(apps_package).__path__[0]

    for root, dirs, files in os.walk(apps_folder):
        for package_name in dirs:
            install_app_settings('.'.join([apps_package, package_name]))
        for module_name in files:
            if module_name[0] != '_' and module_name[-3:] == '.py':
                install_app_settings('.'.join([apps_package, module_name[:-3]]))
        break

    sys.stdout.write(smart_str('All settings from "%s" were installed.\n\n' % apps_package))


def cleanup_settings():
    '''
    Clean-up settings from the "OrderedItem"s and "ListFragment"s
    '''
    for key in dir(settings):
        val = getattr(settings, key)
        if isinstance(val, (list, tuple)):
            res = []
            for i in val:
                if isinstance(i, OrderedItem):
                    res.append(i.content)
                else:
                    res.append(i)
            val = val.__class__(res)
            setattr(settings, key, val)
        if isinstance(val, ListFragment):
            setattr(settings, key, list(val))
