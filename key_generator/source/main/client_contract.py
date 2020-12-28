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

import abc

from shared.keys_entity import KeysEntity


class ClientPresentContract:

    @abc.abstractmethod
    def create_asymmetric_keys(self, supported_algorithm: str):
        pass


class ClientViewContract:

    @abc.abstractmethod
    def show_keys(self, keys: KeysEntity):
        pass

    @abc.abstractmethod
    def set_presenter(self, client_presenter_contract: ClientPresentContract):
        pass
