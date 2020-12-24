import abc

from asymmetric_presenter import AsymmetricPresenterContract
from keys_entity import KeysEntity


class ClientViewContract:

    @abc.abstractmethod
    def show_keys(self, keys: KeysEntity):
        return


class ClientPresentContract:

    @abc.abstractmethod
    def create_algorithm(self, asymmetric_algorithm: AsymmetricPresenterContract):
        return
