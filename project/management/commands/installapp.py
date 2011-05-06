from django.core.management.base import LabelCommand, CommandError

class Command(LabelCommand):
    help = "Install Django app into the project. This app should appear on the PYTHONPATH."
    args = "[appname]"
    label = "application name"

    def handle_label(self, app_name, **options):
        pass