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

from unittest import mock
from unittest.mock import MagicMock

from algorithm.asymmetric.asymmetric_algorithm_contract import AsymmetricAlgorithmContract
from main import ClientViewContract
from main.presenter import MainPresenter
from shared.keys_entity import KeysEntity


@mock.patch("algorithm.asymmetric.asymmetric_algorithm_contract.AsymmetricAlgorithmContract.create_keys")
@mock.patch("main.ClientViewContract.show_keys")
def test_when_provided_valid_algorithm_type_is_expected_call_view(asymmetric_contract_create_key_mock: MagicMock,
                                                                  client_view_contract_show_keys_mock: MagicMock):
    asymmetric_contract_create_key_mock.return_value = KeysEntity('public_key', 'private_key')

    client_view_contract_mock = ClientViewContract()
    asymmetric_algorithm_contract_mock = AsymmetricAlgorithmContract()
    main_presenter = MainPresenter(client_view_contract_mock, asymmetric_algorithm_contract_mock)
    main_presenter.create_asymmetric_keys('open_ssl')

    asymmetric_contract_create_key_mock.assert_called_once()
    client_view_contract_show_keys_mock.assert_called_once()
