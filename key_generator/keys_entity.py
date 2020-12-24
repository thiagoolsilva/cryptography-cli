class KeysEntity:

    public_key = None
    private_key = None

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def __str__(self):
        return ''.join([self.private_key, '\n', self.public_key])
