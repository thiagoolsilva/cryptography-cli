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
from algorithm.asymmetric.supported_asymmetric_algorithm import SupportedAsymmetricAlgorithm
from main import ClientViewContract, ClientPresentContract
from shared.keys_entity import KeysEntity


class MainPresenter(ClientPresentContract):

    def __init__(self, client_view_contract: ClientViewContract, asymmetric_contract: AsymmetricAlgorithmContract):
        self.asymmetric_contract = asymmetric_contract
        self.client_view_contract = client_view_contract
        # attach presenter to provided view
        client_view_contract.set_presenter(self)

    def create_asymmetric_keys(self, supported_algorithm: str):
        keys = KeysEntity('', '')
        if self.asymmetric_contract:
            supported_algorithm_enum = SupportedAsymmetricAlgorithm[supported_algorithm]
            keys = self.asymmetric_contract.create_keys(supported_algorithm_enum)

        if self.client_view_contract:
            self.client_view_contract.show_keys(keys)
