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

import click

from main import MainFactoryDependencies
from main.presenter import MainPresenter
from main.view import Main


@click.command()
@click.option('--algorithm',
              type=click.Choice(['rsa'], case_sensitive=False), required=True, help="Algorithm type")
@click.option('--key_size',
              default=2048, required=True, type=int, help="The output format keys.")
@click.option('--format',
              type=click.Choice(['open_ssl', 'decrypted_open_ssl'], case_sensitive=False), required=True,
              help="The output format to be used.")
def main(algorithm, format, key_size):
    main = Main()
    rsa_algorithm = MainFactoryDependencies().create_asymmetric_cryptography_dependency(algorithm, key_size)
    MainPresenter(main, rsa_algorithm)

    main.create_asymmetric_key(format)


if __name__ == '__main__':
    hello()
