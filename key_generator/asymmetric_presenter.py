import abc


class AsymmetricPresenterContract:

    @abc.abstractmethod
    def create_keys(self, supported_format):
        return
