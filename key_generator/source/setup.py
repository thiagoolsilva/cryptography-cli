#  Copyright (c) 2020  Thiago Lopes da Silva
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import find_packages, setup

from client.build_params import __description__, __license__, __author__, __platform__, __download_url, __app_name__, \
    __author_email, __long_description, __install_requirements__
from client.version import __version__

setup(
    name=__app_name__,
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license=__license__,
    platforms=__platform__,
    author=__author__,
    author_email=__author_email,
    description=__description__,
    long_description=__long_description,
    url=__download_url,
    download_url=__download_url,
    install_requires=__install_requirements__,
    entry_points='''
        [console_scripts]
        key-generator=client.client_script:start_point
    ''',
)
