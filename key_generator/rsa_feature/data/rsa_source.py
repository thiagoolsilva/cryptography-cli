from keys_entity import KeysEntity
from rsa_data_source_contract import RsaDataSourceContract
from data.rsa_creator import RsaCreator
from cryptography.hazmat.primitives import serialization


class RsaSource(RsaDataSourceContract):

    def __init__(self, key_size):
        super().__init__(key_size)
        self.rsa_core = RsaCreator().create_product()

    def create_open_ssl_keys(self) -> KeysEntity:
        rsa_core = self.__create_keys()

        rsa_private_key = rsa_core.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ).decode("utf-8")

        rsa_public_key = rsa_core.public_key().public_bytes(
            serialization.Encoding.OpenSSH,
            serialization.PublicFormat.OpenSSH
        ).decode("utf-8")

        return KeysEntity(rsa_public_key, rsa_private_key)

    def create_open_ssl_decrypted_keys(self) -> KeysEntity:
        rsa_core = self.__create_keys()

        rsa_private_key = rsa_core.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ).decode("utf-8")

        rsa_public_key = rsa_core.public_key().public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo)\
            .decode("utf-8")

        return KeysEntity(rsa_public_key, rsa_private_key)

    def __create_keys(self):
        return self.rsa_core.create_asymmetric_key(self.key_size)
