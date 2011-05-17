import os
import re
import shutil
from random import choice
from django.utils.importlib import import_module
from django.core.management.base import LabelCommand, CommandError
import project


class Command(LabelCommand):
    help = "Creates django-project template with given name in current folder."
    args = "[projectname]"
    label = 'project name'
    can_import_settings = False
    requires_model_validation = False
    
    labels = None
    options = None
    parent_dir = ''
    
    def handle(self, *labels, **options):
        self.labels = labels
        self.options = options
        self.parent_dir = os.getcwd()
        return super(Command, self).handle(*labels, **options)
    
    def handle_label(self, project_name, **options):
        self.stdout.write(u'\nCreating django-project "%s"...\n' % project_name)
        project_dir = self.create_project_dir(project_name)
        self.copy_project_template(project_dir)
        self.cleanup_project(project_dir)
        self.update_project_files(project_dir)
        self.stdout.write(u'django-project "%s" successfully created!\n' % project_name)

    def create_project_dir(self, project_name):
        self.stdout.write(u'  - Creating folder/package "%s"...\n' % project_name)
        self.check_package_name(project_name)
        self.check_project_name(project_name)
        project_dir = os.path.join(self.parent_dir, project_name)
        try:
            os.mkdir(project_dir)
        except OSError, e:
            raise CommandError(e)
        return project_dir
    
    def check_package_name(self, project_name):
        '''
        Check Python package name availability
        '''
        try:
            import_module(project_name)
        except ImportError:
            pass
        else:
            raise CommandError("%r conflicts with the name of an existing Python module and cannot be used as a project name. Please try another name." % project_name)
    
    def check_project_name(self, project_name):
        '''
        Validate project name
        '''
        if not re.search(r'^[_a-zA-Z]\w*$', project_name): # If it's not a valid directory name.
            # Provide a smart error message, depending on the error.
            if not re.search(r'^[_a-zA-Z]', project_name):
                message = 'make sure the name begins with a letter or underscore'
            else:
                message = 'use only numbers, letters and underscores'
            raise CommandError("%r is not a valid project name. Please %s." % (project_name, message))

    def copy_project_template(self, project_dir):
        self.stdout.write('  - Copying django-project template into "%s" ...\n' % project_dir)
        template_dir = os.path.join(project.__path__[0], 'template')
        for path in os.listdir(template_dir):
            shutil.copytree(os.path.join(template_dir, path), os.path.join(project_dir, path))

    IGNORED_DIRS = ['.svn']
    IGNORED_FILES = ['dummy', 'README.txt']
    IGNORED_EXTENSIONS = ['.pyc', '.pyo', '.pyd', '.pyw', '.py.class']

    def cleanup_project(self, project_dir):
        self.stdout.write('  - Cleaning-up "%s" ...\n' % project_dir)
        for d, subdirs, files in os.walk(project_dir):
            for s in subdirs:
                if s in self.IGNORED_DIRS:
                    shutil.rmtree(os.path.join(d, s))
            for f in files:
                if f in self.IGNORED_FILES:
                    os.remove(os.path.join(d, f))
                if os.path.splitext(f) in self.IGNORED_EXTENSIONS:
                    os.remove(os.path.join(d, f))

    def update_project_files(self, project_dir):
        self.update_main_settings(project_dir)

    def update_main_settings(self, project_dir):
        '''
        Create a random SECRET_KEY hash, and put it in the main settings.
        '''
        self.stdout.write('  - Updating main.py...\n')
        main_settings_file = os.path.join(project_dir, 'source', 'conf', 'settings', 'main.py')
        settings_contents = open(main_settings_file, 'r').read()
        fp = open(main_settings_file, 'w')
        secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        settings_contents = re.sub(r"(?<=SECRET_KEY = ')'", secret_key + "'", settings_contents)
        fp.write(settings_contents)
        fp.close()
