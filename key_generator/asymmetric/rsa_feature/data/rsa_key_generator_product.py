from cryptography_product import AsymmetricProduct
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


class RsaKeyGeneratorProduct(AsymmetricProduct):

    def create_asymmetric_key(self, key_size):
        default_exponent = 65537
        private_rsa_key = rsa.generate_private_key(
            default_exponent, key_size, default_backend())

        return private_rsa_key
