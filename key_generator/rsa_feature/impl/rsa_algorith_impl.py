from asymmetric_algorithm_contract import AsymmetricAlgorithmContract
from rsa_feature.user_case import CreateRsaKeyUserCase, SupportedAsymmetricAlgorithm


class RsaAlgorithm(AsymmetricAlgorithmContract):

    def __init__(self,  create_rsa_keys_user_case: CreateRsaKeyUserCase):
        self.create_rsa_user_case = create_rsa_keys_user_case

    def create_keys(self, supported_format: SupportedAsymmetricAlgorithm):
        rsa_keys = self.create_rsa_user_case.create_keys(supported_format)

        return rsa_keys
