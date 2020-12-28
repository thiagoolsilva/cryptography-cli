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

from cryptography.hazmat.primitives import serialization

from algorithm.asymmetric.rsa_feature import RsaDataSourceContract
from algorithm.asymmetric.rsa_feature.data.rsa_creator import RsaCreator
from shared.keys_entity import KeysEntity


class RsaSource(RsaDataSourceContract):

    def __init__(self, key_size):
        super().__init__(key_size)
        self.rsa_core = RsaCreator().create_product()

    def create_open_ssl_keys(self) -> KeysEntity:
        rsa_core = self.__create_keys()

        rsa_private_key = rsa_core.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ).decode("utf-8")

        rsa_public_key = rsa_core.public_key().public_bytes(
            serialization.Encoding.OpenSSH,
            serialization.PublicFormat.OpenSSH
        ).decode("utf-8")

        return KeysEntity(rsa_public_key, rsa_private_key)

    def create_open_ssl_decrypted_keys(self) -> KeysEntity:
        rsa_core = self.__create_keys()

        rsa_private_key = rsa_core.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ).decode("utf-8")

        rsa_public_key = rsa_core.public_key().public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo) \
            .decode("utf-8")

        return KeysEntity(rsa_public_key, rsa_private_key)

    def __create_keys(self):
        return self.rsa_core.create_asymmetric_key(self.key_size)
