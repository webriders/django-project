from project.utils.settings import import_settings
import_settings('conf.live_settings', globals())
import_settings('conf.dev_settings', globals())