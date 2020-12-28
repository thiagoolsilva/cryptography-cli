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

from algorithm.asymmetric.rsa_feature import RsaRepositoryContract
from algorithm.asymmetric.rsa_feature.impl import RsaAlgorithm
from algorithm.asymmetric.rsa_feature.user_case.create_rsa_keys_use_case import CreateRsaKeyUserCase
from algorithm.asymmetric.supported_asymmetric_algorithm import SupportedAsymmetricAlgorithm
from shared.keys_entity import KeysEntity


@mock.patch("algorithm.asymmetric.rsa_feature.user_case.create_rsa_keys_use_case.CreateRsaKeyUserCase.create_keys")
def test_when_provided_valid_supported_asymmetric_algorithm(create_keys_mock: MagicMock):
    create_keys_mock.return_value = KeysEntity('public_key', 'private_key')

    rsa_repository = RsaRepositoryContract()
    create_rsa_keys_user_case = CreateRsaKeyUserCase(rsa_repository)

    rsa_algorithm_impl = RsaAlgorithm(create_rsa_keys_user_case)
    result_set = rsa_algorithm_impl.create_keys(SupportedAsymmetricAlgorithm.open_ssl)

    create_keys_mock.assert_called_once()
    assert result_set is not None
