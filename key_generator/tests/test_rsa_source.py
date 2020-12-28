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

from algorithm.asymmetric.rsa_feature.data.rsa_source import RsaSource


def test_when_call_create_open_ssl_keys_is_expected_to_return_valid_keys():
    rsa_source = RsaSource(1024)
    encrypted_pem_keys = rsa_source.create_open_ssl_keys()

    assert encrypted_pem_keys is not None
    assert encrypted_pem_keys.public_key is not None
    assert encrypted_pem_keys.private_key is not None


def test_when_call_create_open_ssl_decrypted_keys_is_expected_to_return_valid_keys():
    rsa_source = RsaSource(1024)
    decrypted_pem_keys = rsa_source.create_open_ssl_decrypted_keys()

    assert decrypted_pem_keys is not None
    assert decrypted_pem_keys.public_key is not None
    assert decrypted_pem_keys.private_key is not None
