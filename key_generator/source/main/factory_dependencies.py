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

from algorithm.asymmetric.asymmetric_algorithm_contract import AsymmetricAlgorithmContract
from algorithm.asymmetric.rsa_feature.data import RsaRepository
from algorithm.asymmetric.rsa_feature.data.rsa_source import RsaSource
from algorithm.asymmetric.rsa_feature.impl import RsaAlgorithm
from algorithm.asymmetric.rsa_feature.user_case.create_rsa_keys_use_case import CreateRsaKeyUserCase

SUPPORTED_RSA_ALGORITHM = 'rsa'


class MainFactoryDependencies:

    def create_asymmetric_cryptography_dependency(self,
                                                  algorithm_type: str,
                                                  key_size: int) -> AsymmetricAlgorithmContract:
        """
        Create cryptography dependencies

        :param algorithm_type: supported algorithm type
        :param key_size: key size used to generate the key
        :return: AsymmetricPresenterContract with its dependencies
        """
        if algorithm_type == SUPPORTED_RSA_ALGORITHM:
            algorithm_dependencies = self.__create_rsa_dependencies(key_size)
        else:
            raise TypeError("algorithm not supported")

        return algorithm_dependencies

    @staticmethod
    def __create_rsa_dependencies(key_size: int) -> AsymmetricAlgorithmContract:
        """
        create rsa dependencies
        :param key_size: key size used to generate the key
        :return: RsaPresenter with its dependencies
        """
        rsa_data_source = RsaSource(key_size)
        rsa_repository = RsaRepository(rsa_data_source)
        create_rsa_key_user_case = CreateRsaKeyUserCase(rsa_repository)
        return RsaAlgorithm(create_rsa_key_user_case)
