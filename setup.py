#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
rmock
-----

rmock is an test tool for adexchange.

"""

import ast
import os
import os.path
import re
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')
data_dir = 'rmock/res'
data = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

with open('rmock/__init__.py', 'rb') as f:
        version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))
        setup(
            name='rmock',
            version=version,
            url='http://git.adleida.com/paxp/',
            author='adleida',
            author_email='noreply@adleida.com',
            description='rmock is an test tool for adexchange.',
            long_description=__doc__,
            packages=['rmock', 'rmock.ext'],
            package_data={'rmock': data},
            include_package_data=True,
            zip_safe=False,
            platforms='any',
            entry_points='''
                [console_scripts]
                rmock=rmock.mock:main
            ''',
            install_requires=[
                'Flask==0.10.1',
                'PyYAML==3.11',
                'termcolor==1.1.0'
            ],
        )
