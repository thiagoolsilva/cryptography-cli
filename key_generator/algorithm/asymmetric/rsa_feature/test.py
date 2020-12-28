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

from algorithm.asymmetric.rsa_feature.data import RsaRepository
from algorithm.asymmetric.rsa_feature.data.rsa_source import RsaSource

rsa_data_source = RsaSource(2048)
rsa_repository = RsaRepository(rsa_data_source)

keys = rsa_repository.create_open_ssl_keys()

print(keys.private_key)
print(keys.public_key)
