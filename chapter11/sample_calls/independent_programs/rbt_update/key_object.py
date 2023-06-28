

# key_object.py


class KeyObject:
    """Used for testing anything that requires a key."""
    def __init__(self, string, key):
        self.string = string
        self.key = key
    @staticmethod
    def get_key(x):
        return x.key
    @staticmethod
    def set_key(x, key):
        x.key = key
    def __gt__(self, obj):
        return self.key > obj.key
    def __str__(self):
        return self.string


# Testing
if __name__ == '__main__':
    obja = KeyObject('a', 1)
    objb = KeyObject('b', 2)
    print(obja < objb)
    print(obja > objb)