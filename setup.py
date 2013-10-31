# Based on Django "How to write reusable apps" tutorial.

import os
import setuptools

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='django-conferenceabstract',
    version='0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A Django app to manage conference abstract submissions.',
    long_description=README,
    #url='http://www.example.com/',
    author='Jeremy Muhlich',
    author_email='jmuhlich@bitflood.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
