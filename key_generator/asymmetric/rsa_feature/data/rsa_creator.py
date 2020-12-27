from asymmetric.rsa_feature.data import RsaKeyGeneratorProduct
from cryptography_algorithm_creator import AsymmetricCreator


class RsaCreator(AsymmetricCreator):

    def create_product(self):
        return RsaKeyGeneratorProduct()
