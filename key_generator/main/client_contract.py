import abc

from keys_entity import KeysEntity


class ClientPresentContract:

    @abc.abstractmethod
    def create_asymmetric_keys(self, supported_algorithm: str):
        return


class ClientViewContract:

    @abc.abstractmethod
    def show_keys(self, keys: KeysEntity):
        return

    @abc.abstractmethod
    def set_presenter(self, client_presenter_contract: ClientPresentContract):
        return
