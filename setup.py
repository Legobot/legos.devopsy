# Legos, A namespace package for distribution of Legobot plugins
# Copyright (C) 2017  Brenton Briggs II

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
descrption = '[devops|security|dba|etc]reactions fetcher plugin for Legobot'
name = 'legos.devopsy'
setup(
    name=name,
    version='0.1.0',
    namespace_packages=name.split('.')[:-1],
    license='GPLv3',
    descrption='[devops|security|dba|etc]reactions fetcher plugin for Legobot',
    author='Brenton Briggs II',
    url='https://github.com/bbriggs/' + name,
    install_requires=['legobot>=1.0.1',
                      'pyquery'
                      ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3'
    ],
    packages=find_packages()
)
