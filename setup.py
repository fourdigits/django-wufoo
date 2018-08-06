import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-wufoo',
    version='0.3',
    packages=['django_wufoo', 'django_wufoo.management', 'django_wufoo.management.commands'],
    include_package_data=True,
    license='MIT License',
    description='Django app that synchronizes Wufoo forms (one-Way) to your database.',
    long_description=README,
    url='https://github.com/stetelepta/django-wufoo',
    author='Salmon Tetelepta',
    author_email='salmon@eight.nl',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License http://www.opensource.org/licenses/mit-license.php',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)