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

from algorithm.asymmetric.asymmetric_algorithm_contract import AsymmetricAlgorithmContract
from algorithm.asymmetric.rsa_feature.user_case.create_rsa_keys_use_case import CreateRsaKeyUserCase
from algorithm.asymmetric.supported_asymmetric_algorithm import SupportedAsymmetricAlgorithm


class RsaAlgorithm(AsymmetricAlgorithmContract):

    def __init__(self,  create_rsa_keys_user_case: CreateRsaKeyUserCase):
        self.create_rsa_user_case = create_rsa_keys_user_case

    def create_keys(self, supported_format: SupportedAsymmetricAlgorithm):
        rsa_keys = self.create_rsa_user_case.create_keys(supported_format)

        return rsa_keys
