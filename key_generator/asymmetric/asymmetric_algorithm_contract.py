import abc

from keys_entity import KeysEntity


class AsymmetricAlgorithmContract:

    @abc.abstractmethod
    def create_keys(self, supported_format: str) -> KeysEntity:
        return
