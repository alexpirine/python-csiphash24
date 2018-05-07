from codecs import open
from os import path

from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()


setup(
    name='csiphash24',
    version='1.0',

    description='A CFFI-based implementation of SipHash24',
    long_description=readme,
    url='https://github.com/alexpirine/python-csiphash24',

    author='Alexandre Syenchuk',
    author_email='alex@pirine.fr',
    license='MIT',

    packages=find_packages(exclude=['test']),

    setup_requires=["cffi>=1.4.0"],
    cffi_modules=["build_csiphash24.py:ffibuilder"],
    install_requires=["cffi>=1.4.0"],
)
