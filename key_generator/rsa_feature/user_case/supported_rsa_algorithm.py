from enum import Enum


class SupportedRsaAlgorithm(Enum):
    OPEN_SSL_FORMAT = 'open_ssl',
    DECRYPTED_OPEN_SSL_FORMAT = 'decrypted_open_ssl'
