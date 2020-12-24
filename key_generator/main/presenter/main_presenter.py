from asymmetric_algorithm_contract import AsymmetricAlgorithmContract
from keys_entity import KeysEntity
from main import ClientViewContract, ClientPresentContract
from rsa_feature.user_case import SupportedAsymmetricAlgorithm


class MainPresenter(ClientPresentContract):

    def __init__(self, client_view_contract: ClientViewContract, asymmetric_contract: AsymmetricAlgorithmContract):
        self.asymmetric_contract = asymmetric_contract
        self.client_view_contract = client_view_contract
        # attach presenter to provided view
        client_view_contract.set_presenter(self)

    def create_asymmetric_keys(self, supported_algorithm: str):
        keys = KeysEntity('', '')
        if self.asymmetric_contract:
            supported_algorithm_enum = SupportedAsymmetricAlgorithm[supported_algorithm]
            keys = self.asymmetric_contract.create_keys(supported_algorithm_enum)

        if self.client_view_contract:
            self.client_view_contract.show_keys(keys)
