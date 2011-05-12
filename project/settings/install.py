from project.settings.utils.lists import merge
from project.settings.utils.modules import get_module_constants_dict
from project.settings.utils import get_option, get_default_option, set_option


def install(module):
    incoming = get_module_constants_dict(module)
    for key, option in incoming.iteritems():
        if isinstance(option, (list, tuple)):
            try:
                xst = get_option(key)
            except AttributeError:
                try:
                    xst = get_default_option(key)
                except AttributeError:
                    xst = []
            set_option(key, merge(xst, option))
        else:
            set_option(key, option)

