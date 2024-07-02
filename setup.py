from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add any dependencies your package needs
    entry_points={
        'console_scripts': [
            'mypackage-cli = mypackage.module_name:main_func',
        ],
    },
    # Other metadata
    author='Lea Runesha',
    author_email='lgr2sge@virginia.edu',
    description='in class activity on july 02',
    url='https://github.com/learunesha/inclass-july02', 
)


