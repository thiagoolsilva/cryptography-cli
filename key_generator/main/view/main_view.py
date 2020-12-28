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

from keys_entity import KeysEntity
from main import ClientViewContract, ClientPresentContract


class Main(ClientViewContract):

    client_presenter: ClientPresentContract

    def set_presenter(self, client_presenter: ClientPresentContract):
        self.client_presenter = client_presenter

    def create_asymmetric_key(self, supported_algorithm: str):
        self.client_presenter.create_asymmetric_keys(supported_algorithm)

    def show_keys(self, keys: KeysEntity):
        print(keys)
