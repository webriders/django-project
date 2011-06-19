import sys

def settings_required():
    settings_set = False
    for k in sys.argv:
        if k.split('=')[0] == '--settings':
            settings_set = True
    if not settings_set:
        sys.stderr.write('There is no settings specified (default was turned off)\nPlease, specify --settings parameter.')
        sys.exit(1)

settings_required()