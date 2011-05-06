import platform
from project.utils.settings import import_settings

import_settings('conf.main_settings', globals())

DEPLOYMENT = False
# Provide some deployment server detection
DEPLOYMENT_SERVERS = ('servername',)
DEPLOYMENT = platform.node() in DEPLOYMENT_SERVERS

if DEPLOYMENT:
    import_settings('conf.live_settings', globals())
else:
    import_settings('conf.dev_settings', globals())

del import_settings