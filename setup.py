"""
A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages
from os import path
import codecs
import os
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

with codecs.open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'py_leap_api',
            '__init__.py'
        ), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name='py_leap_api',
    version=version,
    description='Unofficial Library to interact with TryLeap REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/IperGiove/py_leap_api',
    author='ipergiove',
    author_email='ipergiove@duck.com',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Project Audience
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Project License
        'License :: OSI Approved :: Apache Software License',

        # Python versions (not enforced)
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='Leap,api,genrative,image',
    packages=find_packages(exclude=['examples', 'tests', 'docs']),
    # Python versions (enforced)
    python_requires='>=3.0.0, <4',
    # deps installed by pip
    install_requires=[
        'httpx~=0.21.1',
    ],
    project_urls={
        'Doc': 'https://docs.tryleap.ai/reference/inferencescontroller_create-1',
        'Source': 'https://github.com/IperGiove/py_leap_api',
    },
)
