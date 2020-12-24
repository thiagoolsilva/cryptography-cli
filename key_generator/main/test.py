from main import Main, MainFactoryDependencies
from main.presenter import MainPresenter
from rsa_feature.user_case import SupportedAsymmetricAlgorithm

main = Main()
rsa_algorithm = MainFactoryDependencies().create_asymmetric_cryptography_dependency('rsa', 2048)
presenter = MainPresenter(main, rsa_algorithm)

#  create openSSL keys
main.create_asymmetric_key('OPEN_SSL_FORMAT')

# test = SupportedAsymmetricAlgorithm['OPEN_SSL_FORMAT']
# print(test)

