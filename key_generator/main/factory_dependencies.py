from asymmetric_algorithm_contract import AsymmetricAlgorithmContract
from rsa_feature.data import RsaRepository
from rsa_feature.data.rsa_source import RsaSource
from rsa_feature.impl.rsa_algorith_impl import RsaAlgorithm
from rsa_feature.user_case import CreateRsaKeyUserCase

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
s        :param key_size: key size used to generate the key
        :return: RsaPresenter with its dependencies
        """
        rsa_data_source = RsaSource(key_size)
        rsa_repository = RsaRepository(rsa_data_source)
        create_rsa_key_user_case = CreateRsaKeyUserCase(rsa_repository)
        return RsaAlgorithm(create_rsa_key_user_case)
