#import platform
#from project.utils.settings import import_settings
#
#import_settings(globals())
#
#DEPLOYMENT = False
## Provide some deployment server detection
#DEPLOYMENT_SERVERS = ('servername',)
#DEPLOYMENT = platform.node() in DEPLOYMENT_SERVERS
#
#if DEPLOYMENT:
#    import_settings('conf.settings.live', globals())
#else:
#    import_settings('conf.settings.dev', globals())
#
#del import_settings