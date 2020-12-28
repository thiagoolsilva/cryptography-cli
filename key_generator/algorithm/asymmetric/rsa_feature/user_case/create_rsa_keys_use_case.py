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

from algorithm.asymmetric.rsa_feature import RsaRepositoryContract
from algorithm.asymmetric.supported_asymmetric_algorithm import SupportedAsymmetricAlgorithm
from keys_entity import KeysEntity


class CreateRsaKeyUserCase:

    def __init__(self, rsa_repository_contract: RsaRepositoryContract):
        self.rsa_repository = rsa_repository_contract

    def create_keys(self, supported_rsa_algorithm: SupportedAsymmetricAlgorithm) -> KeysEntity:
        rsa_keys = None
        if supported_rsa_algorithm == SupportedAsymmetricAlgorithm.open_ssl:
            rsa_keys = self.rsa_repository.create_open_ssl_keys()
        elif supported_rsa_algorithm == SupportedAsymmetricAlgorithm.decrypted_open_ssl:
            rsa_keys = self.rsa_repository.create_open_ssl_decrypted_keys()

        return rsa_keys
