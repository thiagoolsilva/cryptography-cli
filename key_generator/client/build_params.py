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

import os
import pathlib

import pkg_resources


def load_install_requirements():
    with pathlib.Path('requirements.txt').open() as requirements_txt:
        install_requires = [
            str(requirement)
            for requirement
            in pkg_resources.parse_requirements(requirements_txt)
        ]
    return install_requires


def load_long_description():
    current_directory = os.path.dirname(os.getcwd())
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


__app_name__ = 'key-generator-cli'
__description__ = 'it is a CLI program used to generate private and public keys by provided algorithms.'
__author__ = 'Thiago Lopes da Silva'
__author_email = 'thiagoolsilva@gmail.com'
__license__ = 'https://github.com/thiagoolsilva/cryptography-cli/blob/main/LICENSE'
__download_url = 'https://github.com/thiagoolsilva/cryptography-cli'
__platform__ = 'any'
__long_description = load_long_description()
__install_requirements__ = load_install_requirements()
