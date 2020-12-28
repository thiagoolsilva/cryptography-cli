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
from algorithm.asymmetric.supported_asymmetric_algorithm import SupportedAsymmetricAlgorithm
from main import MainFactoryDependencies

KEY_SIZE_UT = 1024
RSA_ALGORITHM_UT = 'rsa'


def test_when_provided_invalid_algorithm_is_expected_to_throws_exception():
    with pytest.raises(TypeError):
        MainFactoryDependencies().create_asymmetric_cryptography_dependency('invalid', KEY_SIZE_UT)


def test_when_provided_rsa_algorithm_is_expected_to_return_valid_value():
    asymmetric_algorithm_contract = MainFactoryDependencies().create_asymmetric_cryptography_dependency(
        RSA_ALGORITHM_UT, KEY_SIZE_UT)
    assert asymmetric_algorithm_contract is not None


def test_when_provided_invalid_supported_asymmetric_algorithm_is_expected_to_throws_exception():
    with pytest.raises(TypeError):
        asymmetric_algorithm_contract = MainFactoryDependencies().create_asymmetric_cryptography_dependency(
            RSA_ALGORITHM_UT, KEY_SIZE_UT)
        asymmetric_algorithm_contract.create_keys(None)


def test_when_provided_valid_open_ssl_algorithm_is_expected_to_return_valid_value():
    asymmetric_algorithm_contract = MainFactoryDependencies().create_asymmetric_cryptography_dependency(
        RSA_ALGORITHM_UT, KEY_SIZE_UT)
    keys = asymmetric_algorithm_contract.create_keys(SupportedAsymmetricAlgorithm.open_ssl)

    assert keys is not None
    assert keys.private_key is not None
    assert keys.public_key is not None

