from rsa_feature.data.rsa_repository import RsaRepository
from rsa_feature.data.rsa_source import RsaSource

rsa_data_source = RsaSource(2048)
rsa_repository = RsaRepository(rsa_data_source)

keys = rsa_repository.create_open_ssl_decrypted_keys()

print(keys.private_key)
print(keys.public_key)
