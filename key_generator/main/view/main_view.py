from keys_entity import KeysEntity
from main import ClientViewContract, ClientPresentContract


class Main(ClientViewContract):

    client_presenter: ClientPresentContract

    def set_presenter(self, client_presenter: ClientPresentContract):
        self.client_presenter = client_presenter

    def create_asymmetric_key(self, supported_algorithm: str):
        self.client_presenter.create_asymmetric_keys(supported_algorithm)

    def show_keys(self, keys: KeysEntity):
        print(keys)
