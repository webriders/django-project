import sys
import os
import imp
from django.utils.encoding import smart_str
from project.utils.modules import get_module, get_module_consts
from project.utils.settings import get_setting, set_setting, append_setting
from project.utils.urls import append_urlpatterns


def install_settings(settings_module):
    """
    Install settings from the specified module.
    Only UPPERCASE settings (that doesn't starts with "_") will be installed.
    """
    incoming = get_module_consts(settings_module)

    for key, option in incoming.iteritems():
        set_setting(key, option)


def install_main_settings():
    """
    Shortcut for the:
        install_settings('conf.settings.main')
    """
    return install_settings('conf.settings.main')


def install_app(name=None, conf=None):
    """
    Install django application (settings and urls).

    'app_conf_path' may be presented as:
        * Python module (regular *.py file)
        * Python package (that should contain 'settings.py' inside)
          If it also contains 'urls.py' - this module will be added to the 'URLS_TO_INSTALL' setting

    Conventions:
        * If there is setting named "ignore" and it's bool == True, then installation will be cancelled.
        * See more conventions in the "install_settings" docs - help(install_settings)
    """

    sys.stdout.write(smart_str('Installing "%s" ...\n' % conf))

    if conf:
        try:
            conf_module = get_module(conf)
        except ImportError:
            sys.stderr.write(smart_str('Error: can\'t import "%s" module.' % conf))
            sys.exit(1)

        # App conf may be a package or a module
        if '__init__.py' in conf_module.__file__:
            # Get app settings
            app_settings = '.'.join([conf, 'settings'])
            try:
                app_settings = get_module(app_settings)
            except ImportError:
                app_settings = None

            # Get app urls
            app_urls = '.'.join([conf, 'urls'])
            try:
                imp.find_module('urls', conf_module.__path__)
            except ImportError:
                app_urls = None
        else:
            app_settings = conf_module
            app_urls = None

        if app_settings:
            if getattr(app_settings, 'ignore', False):
                sys.stdout.write(smart_str('... "%s" installation ignored.\n' % conf))
            else:
                install_settings(app_settings)

        if app_urls:
            # Postpone for further urls install
            append_setting('URLS_TO_INSTALL', app_urls)

    if name:
        append_setting('INSTALLED_APPS', name)


def install_apps(apps_package='conf.apps'):
    """
    Installs all applications settings from the specified python package.
    See help(install_app) and help(install_settings) for more info.
    """
    apps_folder = get_module(apps_package).__path__[0]

    for root, dirs, files in os.walk(apps_folder):
        for package_name in dirs:
            install_app('.'.join([apps_package, package_name]))
        for module_name in files:
            if module_name[0] != '_' and module_name[-3:] == '.py':
                install_app('.'.join([apps_package, module_name[:-3]]))
        break

    sys.stdout.write(smart_str('All apps from "%s" were installed.\n\n' % apps_package))


def install_apps_urls():
    stack = get_setting('URLS_TO_INSTALL')
    while stack:
        urls = get_module(stack.pop())
        urlpatterns = getattr(urls, 'urlpatterns', None)
        if urlpatterns:
            append_urlpatterns(urlpatterns)
