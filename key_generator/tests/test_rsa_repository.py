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

from algorithm.asymmetric.rsa_feature import RsaDataSourceContract
from algorithm.asymmetric.rsa_feature.data import RsaRepository


@mock.patch("algorithm.asymmetric.rsa_feature.RsaDataSourceContract.create_open_ssl_keys")
def test_when_call_create_open_ssl_keys_is_expected_to_call_data_source_function(create_open_ssl_keys_mock: MagicMock):
    rsa_data_source_contract = RsaDataSourceContract(1024)
    rsa_repository = RsaRepository(rsa_data_source_contract)

    rsa_repository.create_open_ssl_keys()

    create_open_ssl_keys_mock.assert_called_once()


@mock.patch("algorithm.asymmetric.rsa_feature.RsaDataSourceContract.create_open_ssl_decrypted_keys")
def test_when_call_create_open_ssl_decrypted_keys_is_expected_to_call_data_source_function(
        create_open_ssl_decrypted_keys_mock: MagicMock):
    rsa_data_source_contract = RsaDataSourceContract(1024)
    rsa_repository = RsaRepository(rsa_data_source_contract)

    rsa_repository.create_open_ssl_decrypted_keys()

    create_open_ssl_decrypted_keys_mock.assert_called_once()
