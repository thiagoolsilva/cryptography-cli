from asymmetric_presenter import AsymmetricPresenterContract
from main.client_contract import ClientViewContract
from rsa_feature.user_case import CreateRsaKeyUserCase, SupportedRsaAlgorithm


class RsaPresenter(AsymmetricPresenterContract):

    def __init__(self, client_view_contract: ClientViewContract, create_rsa_keys_user_case: CreateRsaKeyUserCase):
        self.create_rsa_user_case = create_rsa_keys_user_case
        self.client_view_contract = client_view_contract

    def create_keys(self, supported_format: str):
        supported_rsa_algorithm = SupportedRsaAlgorithm[supported_format]
        rsa_keys = self.create_rsa_user_case.create_keys(supported_rsa_algorithm)

        if rsa_keys not None
            self.client_view_contract.show_keys(rsa_keys)
