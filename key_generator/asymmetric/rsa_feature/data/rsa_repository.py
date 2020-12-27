from keys_entity import KeysEntity
from asymmetric.rsa_feature import RsaRepositoryContract, RsaDataSourceContract


class RsaRepository(RsaRepositoryContract):

    def __init__(self, rsa_data_source_contract: RsaDataSourceContract):
        self.rsa_data_source_contract = rsa_data_source_contract

    def create_open_ssl_keys(self) -> KeysEntity:
        return self.rsa_data_source_contract.create_open_ssl_keys()

    def create_open_ssl_decrypted_keys(self) -> KeysEntity:
        return self.rsa_data_source_contract.create_open_ssl_decrypted_keys()