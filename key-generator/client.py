from asymmetric.rsa.rsa_creator import RsaCreator
from key_size.key_length import KeySize


rsaProduct = RsaCreator()
asymmetric_key = rsaProduct.create_product(
).create_asymmetric_key(KeySize.KEY_SIZE_2048.value)
print(asymmetric_key)
