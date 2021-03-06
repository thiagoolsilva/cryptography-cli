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

from algorithm.asymmetric.rsa_feature.data import RsaKeyGeneratorProduct


def test_when_create_asymmetric_key_is_expected_to_return_valid_instance():

    rsa_key_generator_product = RsaKeyGeneratorProduct()
    result_set = rsa_key_generator_product.create_asymmetric_key(1024)

    assert result_set is not None
