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

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from algorithm.cryptography_product import AsymmetricProduct


class RsaKeyGeneratorProduct(AsymmetricProduct):

    def create_asymmetric_key(self, key_size):
        default_exponent = 65537
        private_rsa_key = rsa.generate_private_key(
            default_exponent, key_size, default_backend())

        return private_rsa_key
