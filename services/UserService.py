class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UserService(metaclass=SingletonMeta):
    def __init__(self):
        self.token = ""
        self.id = 0
        self.qrcodeData = []

    def get_id(self):
        return self.id

    def set_id(self, userId):
        self.id = userId

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token

    def get_qrcode_data(self):
        return self.qrcodeData

    def append_qrcode_data(self, qrcodeData):
        self.qrcodeData.append(qrcodeData)