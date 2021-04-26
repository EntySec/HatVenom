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
      zip_safe=False
)

os.system("mkdir ~/.hatvenom")
os.system("cp -r templates ~/.hatvenom")
os.system("cp hatvenom.py /usr/local/bin/hatvenom")
os.system("chmod +x /usr/local/bin/hatvenom")
