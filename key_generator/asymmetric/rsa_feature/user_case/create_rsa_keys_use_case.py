from asymmetric.rsa_feature.user_case.supported_rsa_algorithm import SupportedAsymmetricAlgorithm
from keys_entity import KeysEntity
from asymmetric.rsa_feature import RsaRepositoryContract


class CreateRsaKeyUserCase:

    def __init__(self, rsa_repository_contract: RsaRepositoryContract):
        self.rsa_repository = rsa_repository_contract

    def create_keys(self, supported_rsa_algorithm: SupportedAsymmetricAlgorithm) -> KeysEntity:
        rsa_keys = None
        if supported_rsa_algorithm == SupportedAsymmetricAlgorithm.OPEN_SSL_FORMAT:
            rsa_keys = self.rsa_repository.create_open_ssl_decrypted_keys()
        elif supported_rsa_algorithm == SupportedAsymmetricAlgorithm.DECRYPTED_OPEN_SSL_FORMAT:
            rsa_keys = self.rsa_repository.create_open_ssl_decrypted_keys()

        return rsa_keys
