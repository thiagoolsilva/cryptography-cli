from asymmetric.asymmetric_creator import AsymmetricCreator
from asymmetric.rsa.rsa_key_generator_product import RsaKeyGeneratorProduct


class RsaCreator(AsymmetricCreator):

    def create_product(self):
        return RsaKeyGeneratorProduct()
