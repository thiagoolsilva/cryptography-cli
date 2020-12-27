import abc

from keys_entity import KeysEntity


class RsaDataSourceContract:

    def __init__(self, key_size):
        self.key_size = key_size

    @abc.abstractmethod
    def create_open_ssl_keys(self) -> KeysEntity:
        return

    @abc.abstractmethod
    def create_open_ssl_decrypted_keys(self) -> KeysEntity:
        return


class RsaRepositoryContract:

    @abc.abstractmethod
    def create_open_ssl_keys(self) -> KeysEntity:
        return

    @abc.abstractmethod
    def create_open_ssl_decrypted_keys(self) -> KeysEntity:
        return
