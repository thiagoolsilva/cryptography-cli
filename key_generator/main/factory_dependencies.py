from asymmetric_presenter import AsymmetricPresenterContract
from client_contract import ClientViewContract
from rsa_feature import RsaRepository
from rsa_feature.data import RsaSource
from rsa_feature.presenter.rsa_presenter import RsaPresenter
from rsa_feature.user_case import CreateRsaKeyUserCase

SUPPORTED_RSA_ALGORITHM = 'rsa'


class MainFactoryDependencies:

    

    def create_cryptography_dependency(self, client_view_contract: ClientViewContract,
                                       algorithm_type: str,
                                       key_size: int) -> AsymmetricPresenterContract:
        """
        Create cryptography dependencies

        :param client_view_contract: client view contract that will be used to send back to the view the data retrieved
        from model's layer
        :param algorithm_type: supported algorythm type
        :param key_size: key size used to generate the key
        :return: AsymmetricPresenterContract with its dependencies
        """
        if algorithm_type == SUPPORTED_RSA_ALGORITHM:
            algorithm_dependencies = self.__create_rsa_dependencies(client_view_contract, key_size)
        else:
            raise TypeError("algorithm not supported")

        return algorithm_dependencies

    def __create_rsa_dependencies(self, client_view_contract: ClientViewContract,
                                  key_size: int) -> AsymmetricPresenterContract:
        """
        create rsa dependencies
        :param client_view_contract: client view contract that will be used to send back to the view the data retrieved
        from model's layer
        :param key_size: key size used to generate the key
        :return: RsaPresenter with its dependencies
        """
        rsa_data_source = RsaSource(key_size)
        rsa_repository = RsaRepository(rsa_data_source)
        create_rsa_key_user_case = CreateRsaKeyUserCase(rsa_repository)
        return RsaPresenter(client_view_contract, create_rsa_key_user_case)
