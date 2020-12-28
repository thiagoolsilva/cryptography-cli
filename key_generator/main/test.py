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

from main import MainFactoryDependencies
from main.presenter import MainPresenter
from main.view import Main

main = Main()
rsa_algorithm = MainFactoryDependencies().create_asymmetric_cryptography_dependency('rsa', 2048)
presenter = MainPresenter(main, rsa_algorithm)

#  create openSSL keys
main.create_asymmetric_key('open_ssl')

# test = SupportedAsymmetricAlgorithm['open_ssl']
# print(test)

