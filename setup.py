from setuptools import setup, find_packages

setup(
    name='django-project',
    version="0.7",
    author='Rostyslav Bryzgunov',
    author_email='kottenator@gmail.com',
    description='Modular & scalable Django project template',
    url='http://github.com/kottenator/django-project',
    install_requires=[
        'django',
    ],
    scripts=['project/bin/django-project.py'],
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)