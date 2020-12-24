from cryptography_algorithm_creator import AsymmetricCreator
from rsa_feature.data import RsaKeyGeneratorProduct


class RsaCreator(AsymmetricCreator):

    def create_product(self):
        return RsaKeyGeneratorProduct()
