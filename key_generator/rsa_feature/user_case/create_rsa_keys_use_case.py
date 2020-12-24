from keys_entity import KeysEntity
from rsa_feature import RsaRepositoryContract
from rsa_feature.user_case.supported_rsa_algorithm import SupportedRsaAlgorithm


class CreateRsaKeyUserCase:

    def __init__(self, rsa_repository_contract: RsaRepositoryContract):
        self.rsa_repository = rsa_repository_contract

    def create_keys(self, supported_rsa_algorithm: SupportedRsaAlgorithm) -> KeysEntity:
        rsa_keys = None
        if supported_rsa_algorithm == SupportedRsaAlgorithm.OPEN_SSL_FORMAT:
            rsa_keys = self.rsa_repository.create_open_ssl_decrypted_keys()
        elif supported_rsa_algorithm == SupportedRsaAlgorithm.DECRYPTED_OPEN_SSL_FORMAT:
            rsa_keys = self.rsa_repository.create_open_ssl_decrypted_keys()

        return rsa_keys
