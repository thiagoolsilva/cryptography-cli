from main import MainFactoryDependencies
from main.presenter import MainPresenter
from main.view import Main

main = Main()
rsa_algorithm = MainFactoryDependencies().create_asymmetric_cryptography_dependency('rsa', 2048)
presenter = MainPresenter(main, rsa_algorithm)

#  create openSSL keys
main.create_asymmetric_key('OPEN_SSL_FORMAT')

# test = SupportedAsymmetricAlgorithm['OPEN_SSL_FORMAT']
# print(test)

