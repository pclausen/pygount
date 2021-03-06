"""
Setup for pygount.

Developer cheat sheet
---------------------

Tag a release (simply replace ``0.x`` with the current version number)::

  $ git tag -a -m "Tagged version 0.x." v0.x
  $ git push --tags

Upload release to PyPI::

  $ python3 setup.py bdist_wheel upload
"""
# Copyright (c) 2016, Thomas Aglassinger.
# All rights reserved. Distributed under the BSD License.
import os
from setuptools import setup, find_packages

from pygount import __version__


# Read the long description from the README file.
_setup_folder = os.path.dirname(__file__)
with open(os.path.join(_setup_folder, "README.rst"), encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="pygount",
    version=__version__,
    description="count source lines of code (SLOC) using pygments",
    long_description=long_description,
    url="https://github.com/roskakori/pygount",
    author="Thomas Aglassinger",
    author_email="roskakori@users.sourceforge.net",
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
    ],
    keywords="code analysis count SLOC",
    packages=find_packages(exclude=["tests"]),
    install_requires=["pygments>=2.0"],
    entry_points={"console_scripts": ["pygount=pygount.command:main"]},
)
