#!/usr/bin/env python3

import os

from setuptools import setup

setup(name='hatvenom',
      version='1.0',
      description='Hatvenom',
      url='http://github.com/EntySec/HatVenom',
      author='EntySec',
      author_email='entysec@gmail.com',
      license='MIT',
      packages=['hatvenom'],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'hatvenom = hatvenom:cli'
        ]
    },
)

os.system("mkdir ~/.hatvenom")
os.system("cp -r templates ~/.hatvenom")
