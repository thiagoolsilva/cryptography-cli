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

import pytest
from algorithm.asymmetric.rsa_feature import RsaRepositoryContract
from algorithm.asymmetric.rsa_feature.user_case.create_rsa_keys_use_case import CreateRsaKeyUserCase
from unittest import mock
from unittest.mock import MagicMock
from algorithm.asymmetric.supported_asymmetric_algorithm import SupportedAsymmetricAlgorithm
from shared.keys_entity import KeysEntity


@mock.patch("algorithm.asymmetric.rsa_feature.RsaRepositoryContract.create_open_ssl_keys")
def test_when_supported_algorithm_is_open_ssl_is_expected_to_call_create_open_ssl_function(
        create_open_ssl_mock: MagicMock):
    create_open_ssl_mock.return_value = KeysEntity('public_key', 'private_key')
    rsa_repository_contract = RsaRepositoryContract()

    create_rsa_key_use_case = CreateRsaKeyUserCase(rsa_repository_contract)
    result_set = create_rsa_key_use_case.create_keys(
        SupportedAsymmetricAlgorithm.open_ssl)

    assert result_set is not None
    assert result_set.public_key is not None
    assert result_set.private_key is not None

    create_open_ssl_mock.assert_called_once()


@mock.patch("algorithm.asymmetric.rsa_feature.RsaRepositoryContract.create_open_ssl_decrypted_keys")
def test_when_supported_algorithm_is_open_ssl_decrypted_is_expected_to_call_create_open_ssl_decrypted_keys_function(
        create_open_ssl_decrypted_keys: MagicMock):
    create_open_ssl_decrypted_keys.return_value = KeysEntity(
        'public_key', 'private_key')
    rsa_repository_contract = RsaRepositoryContract()

    create_rsa_key_use_case = CreateRsaKeyUserCase(rsa_repository_contract)
    result_set = create_rsa_key_use_case.create_keys(
        SupportedAsymmetricAlgorithm.decrypted_open_ssl)

    assert result_set is not None
    assert result_set.public_key is not None
    assert result_set.private_key is not None

    create_open_ssl_decrypted_keys.assert_called_once()


def test_when_provided_invalid_supported_algorithm_enum_is_expected_to_throws_exception():
    with pytest.raises(TypeError):
        rsa_repository_contract = RsaRepositoryContract()

        create_rsa_key_use_case = CreateRsaKeyUserCase(rsa_repository_contract)
        create_rsa_key_use_case.create_keys(None)
