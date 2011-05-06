#!/usr/bin/env python
import sys
from optparse import OptionParser
import project
from project.management.commands.startproject import Command as StartProjectCommand

def main():
    parser = OptionParser(
        usage="%prog [options] [projectname]",
        description='Creates django-project template with given name in current folder.',
        version=project.VERSION,
    )

    parser.add_option('--pythonpath', help='A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".')

    argv = sys.argv[:]
    if len(argv) < 2:
        argv.append('-h')

    (options, args) = parser.parse_args(argv)

    if options.pythonpath:
        sys.path.insert(0, options.pythonpath)

    project_names = args[1:]
    StartProjectCommand().execute(*project_names)

if __name__ == '__main__':
    main()